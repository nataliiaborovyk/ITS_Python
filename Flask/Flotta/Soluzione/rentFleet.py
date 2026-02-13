from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from flask import Flask, jsonify, request, url_for


# -----------------------------
# Domain model
# -----------------------------

ALLOWED_STATUSES = {"available", "rented", "maintenance", "cleaning", "retired"}


class Vehicle(ABC):
    """
    Abstract base class for a generic vehicle managed by the system.
    """

    def __init__(
        self,
        plate_id: str,
        model: str,
        driver_name: str | None,
        registration_year: int,
        status: str,
    ) -> None:
        # driver_name can be a string or None
        self.plate_id = plate_id
        self.model = model
        self.driver_name = driver_name
        self.registration_year = registration_year
        self.status = status

    @abstractmethod
    def vehicle_type(self) -> str:
        """Return the type of vehicle, e.g. 'car' or 'van'."""
        raise NotImplementedError

    @abstractmethod
    def base_cleaning_time(self) -> int:
        """Return ordinary cleaning time in minutes."""
        raise NotImplementedError

    @abstractmethod
    def wear_level(self) -> int:
        """Return average wear level for this type (1..5)."""
        raise NotImplementedError

    def info(self) -> dict[str, int | str | bool | None]:
        return {
            "plate_id": self.plate_id,
            "model": self.model,
            "driver_name": self.driver_name,
            "vehicle_type": self.vehicle_type(),
            "registration_year": self.registration_year,
            "status": self.status,
        }

    def estimated_prep_time(self, factor: float = 1.0) -> int:
        """
        Estimated preparation time before a new rent (cleaning + checks).

        Formula:
          base_cleaning_time() * factor + wear_level() * 15
        """
        minutes = self.base_cleaning_time() * float(factor) + self.wear_level() * 15
        return int(round(minutes))


class Car(Vehicle):
    def __init__(
        self,
        plate_id: str,
        model: str,
        driver_name: str | None,
        registration_year: int,
        status: str,
        doors: int,
        is_cabrio: bool,
    ) -> None:
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.doors = doors
        self.is_cabrio = is_cabrio

    def vehicle_type(self) -> str:
        return "car"

    def base_cleaning_time(self) -> int:
        return 30

    def wear_level(self) -> int:
        # Typical low wear for standard cars
        return 2

    def info(self) -> dict[str, int | str | bool | None]:
        data = super().info()
        data.update({"doors": self.doors, "is_cabrio": self.is_cabrio})
        return data


class Van(Vehicle):
    def __init__(
        self,
        plate_id: str,
        model: str,
        driver_name: str | None,
        registration_year: int,
        status: str,
        max_load_kg: int,
        require_special_license: bool,
    ) -> None:
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.max_load_kg = max_load_kg
        self.require_special_license = require_special_license

    def vehicle_type(self) -> str:
        return "van"

    def base_cleaning_time(self) -> int:
        return 60

    def wear_level(self) -> int:
        # Typical high wear for work vans
        return 5

    def info(self) -> dict[str, int | str | bool | None]:
        data = super().info()
        data.update(
            {
                "max_load_kg": self.max_load_kg,
                "require_special_license": self.require_special_license,
            }
        )
        return data


class FleetManager:
    def __init__(self) -> None:
        self.vehicles: dict[str, Vehicle] = {}

    def add(self, vehicle: Vehicle) -> bool:
        if vehicle.plate_id in self.vehicles:
            return False
        self.vehicles[vehicle.plate_id] = vehicle
        return True

    def get(self, plate_id: str) -> Vehicle | None:
        return self.vehicles.get(plate_id)

    def update(self, plate_id: str, new_vehicle: Vehicle) -> None:
        self.vehicles[plate_id] = new_vehicle

    def patch_status(self, plate_id: str, new_status: str) -> None:
        v = self.vehicles.get(plate_id)
        if v is None:
            return
        v.status = new_status

    def delete(self, plate_id: str) -> bool:
        if plate_id not in self.vehicles:
            return False
        del self.vehicles[plate_id]
        return True

    def list_all(self) -> list[dict[str, int | str | bool | None]]:
        return [v.info() for v in self.vehicles.values()]


# -----------------------------
# Helpers (validation/parsing)
# -----------------------------

def _get_first_present(d: dict[str, Any], *keys: str) -> Any:
    for k in keys:
        if k in d:
            return d[k]
    return None


def _validate_common_fields(payload: dict[str, Any]) -> str | None:
    required = ["plate_id", "model", "registration_year", "status"]
    missing = [k for k in required if k not in payload]
    if missing:
        return f"Missing required fields: {', '.join(missing)}"

    if not isinstance(payload["plate_id"], str) or not payload["plate_id"].strip():
        return "plate_id must be a non-empty string"
    if not isinstance(payload["model"], str) or not payload["model"].strip():
        return "model must be a non-empty string"

    try:
        payload["registration_year"] = int(payload["registration_year"])
    except Exception:
        return "registration_year must be an integer"

    if not isinstance(payload["status"], str) or payload["status"] not in ALLOWED_STATUSES:
        return f"status must be one of: {sorted(ALLOWED_STATUSES)}"

    # driver_name may be None or a string
    if "driver_name" in payload and payload["driver_name"] is not None and not isinstance(payload["driver_name"], str):
        return "driver_name must be a string or null"

    return None


def vehicle_from_json(data: dict[str, Any]) -> Vehicle:
    """
    Create a Vehicle instance (Car or Van) from JSON dict.
    Accepts a few alias keys to be tolerant with minor differences.
    """
    vtype = _get_first_present(data, "type", "vehicle_type", "veichle_type")
    if not isinstance(vtype, str):
        raise ValueError("Missing or invalid 'type' (must be 'car' or 'van')")

    # Normalize common keys (accept id->plate_id, purchase_year->registration_year, customer_name->driver_name)
    if "plate_id" not in data and "id" in data:
        data["plate_id"] = data["id"]
    if "registration_year" not in data and "purchase_year" in data:
        data["registration_year"] = data["purchase_year"]
    if "driver_name" not in data and "customer_name" in data:
        data["driver_name"] = data["customer_name"]

    err = _validate_common_fields(data)
    if err:
        raise ValueError(err)

    plate_id = str(data["plate_id"]).strip()
    model = str(data["model"]).strip()
    driver_name = data.get("driver_name", None)
    registration_year = int(data["registration_year"])
    status = str(data["status"])

    if vtype == "car":
        if "doors" not in data or "is_cabrio" not in data:
            raise ValueError("Car requires fields: doors, is_cabrio")
        try:
            doors = int(data["doors"])
        except Exception:
            raise ValueError("doors must be an integer")
        if not isinstance(data["is_cabrio"], bool):
            raise ValueError("is_cabrio must be a boolean")
        return Car(
            plate_id=plate_id,
            model=model,
            driver_name=driver_name,
            registration_year=registration_year,
            status=status,
            doors=doors,
            is_cabrio=bool(data["is_cabrio"]),
        )

    if vtype == "van":
        if "max_load_kg" not in data or "require_special_license" not in data:
            raise ValueError("Van requires fields: max_load_kg, require_special_license")
        try:
            max_load_kg = int(data["max_load_kg"])
        except Exception:
            raise ValueError("max_load_kg must be an integer")
        if not isinstance(data["require_special_license"], bool):
            raise ValueError("require_special_license must be a boolean")
        return Van(
            plate_id=plate_id,
            model=model,
            driver_name=driver_name,
            registration_year=registration_year,
            status=status,
            max_load_kg=max_load_kg,
            require_special_license=bool(data["require_special_license"]),
        )

    raise ValueError("Unknown type. Use 'car' or 'van'.")


# -----------------------------
# Flask app
# -----------------------------

app = Flask(__name__)
fleet_manager = FleetManager()

# Sample data (at least one Car and one Van)
fleet_manager.add(
    Car(
        plate_id="HA014AS",
        model="Fiat Panda",
        driver_name=None,
        registration_year=2019,
        status="available",
        doors=5,
        is_cabrio=False,
    )
)
fleet_manager.add(
    Van(
        plate_id="CC216FG",
        model="Peugeot Partner",
        driver_name="Luca Neri",
        registration_year=2018,
        status="rented",
        max_load_kg=750,
        require_special_license=False,
    )
)


@app.get("/")
def root():
    return jsonify(
        {
            "message": "Welcome to Rent Service API",
            "links": {
                "vehicles_list": url_for("list_vehicles", _external=False),
                "vehicle_sample": url_for("get_vehicle", plate_id="HA014AS", _external=False),
                "estimate_sample": url_for("get_prep_time", plate_id="HA014AS", factor=2.0, _external=False),
            },
        }
    )


@app.get("/vehicles")
def list_vehicles():
    # Coherent choice: return list of dicts (info())
    return jsonify(fleet_manager.list_all())


@app.get("/vehicles/<plate_id>")
def get_vehicle(plate_id: str):
    v = fleet_manager.get(plate_id)
    if v is None:
        return jsonify({"error": "Vehicle not found"}), 404
    return jsonify(v.info())


@app.get("/vehicles/<plate_id>/prep-time/<factor>")
def get_prep_time(plate_id: str, factor: str):
    v = fleet_manager.get(plate_id)
    if v is None:
        return jsonify({"error": "Vehicle not found"}), 404
    try:
        f = float(factor)
    except Exception:
        return jsonify({"error": "Invalid factor"}), 400

    return jsonify(
        {
            "plate_id": v.plate_id,
            "vehicle_type": v.vehicle_type(),
            "factor": f,
            "estimated_total_minutes": v.estimated_prep_time(f),
        }
    )


@app.post("/vehicles")
def create_vehicle():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be JSON object"}), 400

    try:
        v = vehicle_from_json(data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    ok = fleet_manager.add(v)
    if not ok:
        return jsonify({"error": "Vehicle already exists"}), 400

    return jsonify(v.info()), 201


@app.put("/vehicles/<plate_id>")
def put_vehicle(plate_id: str):
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be JSON object"}), 400

    # Enforce the path id
    data = dict(data)
    data["plate_id"] = plate_id

    try:
        v = vehicle_from_json(data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    # Choose behavior: create if missing (UPSERT)
    fleet_manager.update(plate_id, v)
    return jsonify(v.info())


@app.patch("/vehicles/<plate_id>/status")
def patch_vehicle_status(plate_id: str):
    v = fleet_manager.get(plate_id)
    if v is None:
        return jsonify({"error": "Vehicle not found"}), 404

    data = request.get_json(silent=True)
    if not isinstance(data, dict) or "status" not in data:
        return jsonify({"error": "Body must be JSON with 'status' field"}), 400

    new_status = data["status"]
    if not isinstance(new_status, str) or new_status not in ALLOWED_STATUSES:
        return jsonify({"error": f"status must be one of: {sorted(ALLOWED_STATUSES)}"}), 400

    fleet_manager.patch_status(plate_id, new_status)
    return jsonify(fleet_manager.get(plate_id).info())


@app.delete("/vehicles/<plate_id>")
def delete_vehicle(plate_id: str):
    ok = fleet_manager.delete(plate_id)
    if not ok:
        return jsonify({"error": "Vehicle not found"}), 404
    return jsonify({"deleted": True, "plate_id": plate_id})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
