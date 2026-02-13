import json
import requests

# Assumiamo che l'app Flask di rentFleet.py giri su questa base URL
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
        print("Response text:")
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

    # 2) GET /vehicles (lista veicoli)
    r = requests.get(f"{BASE_URL}/vehicles", headers=headers)
    print_response("GET /vehicles", r)

    # 3) POST /vehicles (aggiunge un nuovo veicolo)
    new_plate_id = "XX999YY"
    post_body = {
        "type": "car",
        "plate_id": new_plate_id,
        "model": "Fiat 500 Cabrio",
        "driver_name": "Mario Rossi",
        "registration_year": 2022,
        "status": "available",
        "doors": 3,
        "is_cabrio": True
    }
    r = requests.post(
        f"{BASE_URL}/vehicles",
        headers=headers,
        data=json.dumps(post_body),
    )
    print_response("POST /vehicles (nuovo veicolo car)", r)

    # 4) GET /vehicles/<plate_id> (verifica creazione)
    r = requests.get(f"{BASE_URL}/vehicles/{new_plate_id}", headers=headers)
    print_response("GET /vehicles/<plate_id>", r)

    # 5) PATCH /vehicles/<plate_id>/status (aggiorna stato)
    patch_body = {"status": "rented"}
    r = requests.patch(
        f"{BASE_URL}/vehicles/{new_plate_id}/status",
        headers=headers,
        data=json.dumps(patch_body),
    )
    print_response("PATCH /vehicles/<plate_id>/status", r)

    # 6) PUT /vehicles/<plate_id> (sostituisce completamente le info)
    # Esempio: sostituiamo il veicolo con un van (full replacement)
    put_body = {
        "type": "van",
        "plate_id": new_plate_id,  # verrà comunque imposto dall'URL
        "model": "Ford Transit",
        "driver_name": None,
        "registration_year": 2021,
        "status": "maintenance",
        "max_load_kg": 1200,
        "require_special_license": True
    }
    r = requests.put(
        f"{BASE_URL}/vehicles/{new_plate_id}",
        headers=headers,
        data=json.dumps(put_body),
    )
    print_response("PUT /vehicles/<plate_id>", r)

    # 7) GET /vehicles/<plate_id>/prep-time/2.0 (stima preparazione)
    r = requests.get(f"{BASE_URL}/vehicles/{new_plate_id}/prep-time/2.0", headers=headers)
    print_response("GET /vehicles/<plate_id>/prep-time/2.0", r)

    # 8) DELETE /vehicles/<plate_id> (elimina)
    r = requests.delete(f"{BASE_URL}/vehicles/{new_plate_id}", headers=headers)
    print_response("DELETE /vehicles/<plate_id>", r)

    # 9) GET /vehicles/<plate_id> (deve dare 404)
    r = requests.get(f"{BASE_URL}/vehicles/{new_plate_id}", headers=headers)
    print_response("GET /vehicles/<plate_id> (dopo delete)", r)
