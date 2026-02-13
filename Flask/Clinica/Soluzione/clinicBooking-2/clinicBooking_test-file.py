import json
import requests

# Assumiamo che l'app Flask di main.py giri su questa base URL
BASE_URL = "http://127.0.0.1:5000"


def print_response(title, response):
    """Utility per stampare in modo leggibile le risposte HTTP."""
    print(f"=== {title} ===")
    print("Status code:", response.status_code)
    try:
        data = response.json()
        print("JSON response:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except ValueError:
        print("No JSON body (raw text):")
        print(response.text)
    print()


if __name__ == "__main__":
    headers = {
        "Content-type": "application/json",
        "Accept": "application/json"
    }

    # 1) GET /
    r = requests.get(f"{BASE_URL}/", headers=headers)
    print_response("GET /", r)

    # 2) GET /bookings (lista iniziale non vuota)
    r = requests.get(f"{BASE_URL}/bookings", headers=headers)
    print_response("GET /bookings", r)

    # 3) POST /bookings (creiamo una nuova prenotazione)
    new_booking_id = "BK-3e67"
    new_exam = {
        "type": "exam",
        "booking_id": new_booking_id,
        "patient_name": "Giulia Verdi",
        "doctor": "Dr. Neri",
        "department": "Radiologia",
        "date": "2026-02-10",
        "time": "09:15",
        "status": "scheduled",
        "exam_type": "RMN",
        "requires_fasting": True
    }
    r = requests.post(
        f"{BASE_URL}/bookings",
        headers=headers,
        data=json.dumps(new_exam),
    )
    print_response("POST /bookings (nuova prenotazione exam)", r)

    # 4) GET /bookings/<booking_id> (verifica creazione)
    r = requests.get(f"{BASE_URL}/bookings/{new_booking_id}", headers=headers)
    print_response("GET /bookings/<booking_id>", r)

    # 5) PATCH /bookings/<booking_id>/status (aggiorna stato)
    patch_body = {"status": "checked_in"}
    r = requests.patch(
        f"{BASE_URL}/bookings/{new_booking_id}/status",
        headers=headers,
        data=json.dumps(patch_body),
    )
    print_response("PATCH /bookings/<booking_id>/status", r)

    # 6) PUT /bookings/<booking_id> (sostituisce completamente la prenotazione)
    put_body = {
        "type": "visit",
        "booking_id": "IGNORED_BY_SERVER",
        "patient_name": "Giulia Verdi",
        "doctor": "Dr. Bianchi",
        "department": "Cardiologia",
        "date": "2026-02-12",
        "time": "11:00",
        "status": "scheduled",
        "visit_reason": "Dolore toracico",
        "first_time": True
    }
    r = requests.put(
        f"{BASE_URL}/bookings/{new_booking_id}",
        headers=headers,
        data=json.dumps(put_body),
    )
    print_response("PUT /bookings/<booking_id>", r)

    # 7) GET /bookings/<booking_id>/wait/1.0 (stima attesa)
    r = requests.get(f"{BASE_URL}/bookings/{new_booking_id}/wait/1.0", headers=headers)
    print_response("GET /bookings/<booking_id>/wait/1.0", r)

    # 8) DELETE /bookings/<booking_id> (elimina)
    r = requests.delete(f"{BASE_URL}/bookings/{new_booking_id}", headers=headers)
    print_response("DELETE /bookings/<booking_id>", r)

    # 9) GET /bookings/<booking_id> (deve dare 404)
    r = requests.get(f"{BASE_URL}/bookings/{new_booking_id}", headers=headers)
    print_response("GET /bookings/<booking_id> (dopo delete)", r)
