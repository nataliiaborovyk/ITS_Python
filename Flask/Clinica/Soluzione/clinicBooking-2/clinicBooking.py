from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from flask import Flask, jsonify, request, url_for


# ==========================
# Classi di dominio
# ==========================

class Booking(ABC):
    """
    Prenotazione astratta: non istanziabile direttamente.
    """

    def __init__(
        self,
        booking_id: str,
        patient_name: str,
        doctor: str,
        department: str,
        date: str,
        time: str,
        status: str,
    ):
        self.booking_id = booking_id
        self.patient_name = patient_name
        self.doctor = doctor
        self.department = department
        self.date = date
        self.time = time
        self.status = status

    @abstractmethod
    def booking_type(self) -> str:
        """Tipo prenotazione: visit / exam"""
        raise NotImplementedError

    @abstractmethod
    def base_duration(self) -> int:
        """Durata standard (minuti)."""
        raise NotImplementedError

    @abstractmethod
    def priority_level(self) -> int:
        """Priorità (1..10)."""
        raise NotImplementedError

    def info(self) -> dict[str, Any]:
        return {
            "booking_id": self.booking_id,
            "patient_name": self.patient_name,
            "doctor": self.doctor,
            "department": self.department,
            "date": self.date,
            "time": self.time,
            "status": self.status,
            "type": self.booking_type(),
        }

    def estimated_wait(self, factor: float = 1.0) -> int:
        """
        Attesa stimata (minuti):
        base_duration() * factor + priority_level() * 5
        """
        wait = self.base_duration() * float(factor) + self.priority_level() * 5
        return int(round(wait))


class MedicalVisit(Booking):
    def __init__(
        self,
        booking_id: str,
        patient_name: str,
        doctor: str,
        department: str,
        date: str,
        time: str,
        status: str,
        visit_reason: str,
        first_time: bool,
    ):
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.visit_reason = visit_reason
        self.first_time = bool(first_time)

    def booking_type(self) -> str:
        return "visit"

    def base_duration(self) -> int:
        # Durata standard tipica di una visita (min)
        return 30 if self.first_time else 20

    def priority_level(self) -> int:
        # Semplice euristica: se motivo contiene parole "urgenti" alza priorità
        reason = (self.visit_reason or "").lower()
        keywords = ["urgente", "dolore", "acuto", "svenimento"]

        for k in keywords:
            if k in reason:
                return 7

        return 5

    def info(self) -> dict[str, Any]:
        base = super().info()
        base["visit_reason"] = self.visit_reason
        base["first_time"] = self.first_time
        return base


class DiagnosticExam(Booking):
    def __init__(
        self,
        booking_id: str,
        patient_name: str,
        doctor: str,
        department: str,
        date: str,
        time: str,
        status: str,
        exam_type: str,
        requires_fasting: bool,
    ):
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.exam_type = exam_type
        self.requires_fasting = bool(requires_fasting)

    def booking_type(self) -> str:
        return "exam"

    def base_duration(self) -> int:
        # Durate indicative in base al tipo di esame
        et = (self.exam_type or "").strip().lower()
        if et in ["ecg", "e.c.g."]:
            return 15
        if et in ["rx", "x-ray", "radiografia"]:
            return 20
        if et in ["rmn", "mri", "tac", "ct"]:
            return 60
        return 30

    def priority_level(self) -> int:
        # Semplice euristica: RMN/TAC spesso più "critiche" o più impegnative
        et = (self.exam_type or "").strip().lower()
        if et in ["rmn", "mri", "tac", "ct"]:
            return 8
        return 7

    def info(self) -> dict[str, Any]:
        base = super().info()
        base["exam_type"] = self.exam_type
        base["requires_fasting"] = self.requires_fasting
        return base


class ClinicHub:
    def __init__(self):
        self.bookings: dict[str, Booking] = {}

    def add(self, booking: Booking) -> bool:
        if booking.booking_id in self.bookings:
            return False
        self.bookings[booking.booking_id] = booking
        return True

    def get(self, booking_id: str) -> Booking | None:
        return self.bookings.get(booking_id)

    def update(self, booking_id: str, new_booking: Booking) -> None:
        self.bookings[booking_id] = new_booking

    def patch_status(self, booking_id: str, new_status: str) -> None:
        b = self.bookings.get(booking_id)
        if b is not None:
            b.status = new_status

    def delete(self, booking_id: str) -> bool:
        if booking_id not in self.bookings:
            return False
        del self.bookings[booking_id]
        return True

    def list_all(self) -> list[dict[str, Any]]:
        return [b.info() for b in self.bookings.values()]


# ==========================
# Setup dati iniziali
# ==========================

clinic_hub = ClinicHub()

clinic_hub.add(
    MedicalVisit(
        booking_id="BK-101",
        patient_name="Mario Rossi",
        doctor="Dr. Bianchi",
        department="Cardiologia",
        date="2026-02-10",
        time="14:30",
        status="scheduled",
        visit_reason="Controllo annuale",
        first_time=False,
    )
)

clinic_hub.add(
    DiagnosticExam(
        booking_id="BK-202",
        patient_name="Giulia Verdi",
        doctor="Dr. Neri",
        department="Radiologia",
        date="2026-02-11",
        time="09:15",
        status="scheduled",
        exam_type="RMN",
        requires_fasting=True,
    )
)

# ==========================
# Flask App
# ==========================

app = Flask(__name__)


def _required_fields_present(payload: dict[str, Any], fields: list[str]) -> tuple[bool, str | None]:
    for f in fields:
        if f not in payload:
            return False, f
    return True, None


def _create_booking_from_json(payload: dict[str, Any], booking_id_override: str | None = None) -> tuple[Booking | None, str | None]:
    """
    Crea l'istanza corretta (MedicalVisit / DiagnosticExam) a partire dal JSON.
    Ritorna (booking, error_message).
    """
    if not isinstance(payload, dict):
        return None, "Invalid JSON body"

    # Campi comuni
    common_fields = ["type", "booking_id", "patient_name", "doctor", "department", "date", "time", "status"]
    ok, missing = _required_fields_present(payload, common_fields)
    if not ok:
        return None, f"Missing field: {missing}"

    b_type = str(payload.get("type")).strip().lower()

    booking_id = str(payload.get("booking_id")).strip()
    if booking_id_override is not None:
        booking_id = booking_id_override  # per PUT /bookings/<booking_id>

    patient_name = str(payload.get("patient_name"))
    doctor = str(payload.get("doctor"))
    department = str(payload.get("department"))
    date = str(payload.get("date"))
    time = str(payload.get("time"))
    status = str(payload.get("status"))

    if b_type == "visit":
        specific_fields = ["visit_reason", "first_time"]
        ok, missing = _required_fields_present(payload, specific_fields)
        if not ok:
            return None, f"Missing field: {missing}"

        visit_reason = str(payload.get("visit_reason"))
        first_time = bool(payload.get("first_time"))

        return MedicalVisit(
            booking_id=booking_id,
            patient_name=patient_name,
            doctor=doctor,
            department=department,
            date=date,
            time=time,
            status=status,
            visit_reason=visit_reason,
            first_time=first_time,
        ), None

    if b_type == "exam":
        specific_fields = ["exam_type", "requires_fasting"]
        ok, missing = _required_fields_present(payload, specific_fields)
        if not ok:
            return None, f"Missing field: {missing}"

        exam_type = str(payload.get("exam_type"))
        requires_fasting = bool(payload.get("requires_fasting"))

        return DiagnosticExam(
            booking_id=booking_id,
            patient_name=patient_name,
            doctor=doctor,
            department=department,
            date=date,
            time=time,
            status=status,
            exam_type=exam_type,
            requires_fasting=requires_fasting,
        ), None

    return None, "Unknown type (expected 'visit' or 'exam')"


# --------------------------
# Route GET
# --------------------------

@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {
            "message": "Clinic Booking Hub API",
            "links": {
                "bookings_list": url_for("list_bookings", _external=False),
                "booking_sample": url_for("get_booking", booking_id="BK-101", _external=False),
                "estimate_sample": url_for("get_wait", booking_id="BK-101", factor=1.0, _external=False),
            },
        }
    )


@app.route("/bookings", methods=["GET"])
def list_bookings():
    return jsonify(clinic_hub.list_all())


@app.route("/bookings/<booking_id>", methods=["GET"])
def get_booking(booking_id: str):
    booking = clinic_hub.get(booking_id)
    if booking is None:
        return jsonify({"error": "booking not found"}), 404
    return jsonify(booking.info())


@app.route("/bookings/<booking_id>/wait/<factor>", methods=["GET"])
def get_wait(booking_id: str, factor: str):
    booking = clinic_hub.get(booking_id)
    if booking is None:
        return jsonify({"error": "booking not found"}), 404

    try:
        f = float(factor)
    except ValueError:
        return jsonify({"error": "factor must be a float"}), 400

    return jsonify(
        {
            "booking_id": booking.booking_id,
            "booking_type": booking.booking_type(),
            "factor": f,
            "estimated_wait_minutes": booking.estimated_wait(f),
        }
    )


# --------------------------
# Route POST
# --------------------------

@app.route("/bookings", methods=["POST"])
def create_booking():
    payload = request.get_json()
    booking, err = _create_booking_from_json(payload)
    if booking is None:
        return jsonify({"error": err}), 400

    if not clinic_hub.add(booking):
        return jsonify({"error": "booking_id already exists"}), 400

    return jsonify(booking.info()), 201


# --------------------------
# Route PUT
# --------------------------

@app.route("/bookings/<booking_id>", methods=["PUT"])
def put_booking(booking_id: str):
    payload = request.get_json()
    booking, err = _create_booking_from_json(payload, booking_id_override=booking_id)
    if booking is None:
        return jsonify({"error": err}), 400

    existed = clinic_hub.get(booking_id) is not None
    clinic_hub.update(booking_id, booking)

    # 200 se update, 201 se creato
    return jsonify(booking.info()), (200 if existed else 201)


# --------------------------
# Route PATCH
# --------------------------

@app.route("/bookings/<booking_id>/status", methods=["PATCH"])
def patch_booking_status(booking_id: str):
    booking = clinic_hub.get(booking_id)
    if booking is None:
        return jsonify({"error": "booking not found"}), 404

    payload = request.get_json()
    if not isinstance(payload, dict):
        return jsonify({"error": "Invalid JSON body"}), 400

    new_status = payload.get("status")
    if not new_status or not isinstance(new_status, str):
        return jsonify({"error": "Missing status"}), 400

    clinic_hub.patch_status(booking_id, new_status)
    return jsonify(clinic_hub.get(booking_id).info())


# --------------------------
# Route DELETE
# --------------------------

@app.route("/bookings/<booking_id>", methods=["DELETE"])
def delete_booking(booking_id: str):
    ok = clinic_hub.delete(booking_id)
    if not ok:
        return jsonify({"error": "booking not found"}), 404

    return jsonify({"deleted": True, "booking_id": booking_id})


if __name__ == "__main__":
    # Avvia il server in debug sulla porta 5000
    app.run(debug=True, host="127.0.0.1", port=5000)
