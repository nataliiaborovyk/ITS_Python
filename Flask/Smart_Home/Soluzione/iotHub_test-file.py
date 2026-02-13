import json
import requests

# Assumiamo che l'app Flask di iotHub.py giri su questa base URL
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

    # 2) GET /devices (lista dispositivi)
    r = requests.get(f"{BASE_URL}/devices", headers=headers)
    print_response("GET /devices", r)

    # 3) POST /devices (aggiunge un nuovo dispositivo)
    new_sn = "SN-3e67"
    post_body = {
        "type": "camera",
        "serial_number": new_sn,
        "brand": "Philips",
        "room": "Living Room",
        "installation_year": 2022,
        "status": "online",
        "resolution": "4K",
        "night_vision": True
    }
    r = requests.post(
        f"{BASE_URL}/devices",
        headers=headers,
        data=json.dumps(post_body),
    )
    print_response("POST /devices (nuovo dispositivo camera)", r)

    # 4) GET /devices/<serial_number> (verifica creazione)
    r = requests.get(f"{BASE_URL}/devices/{new_sn}", headers=headers)
    print_response("GET /devices/<serial_number>", r)

    # 5) PATCH /devices/<serial_number>/status (aggiorna stato)
    patch_body = {"status": "updating"}
    r = requests.patch(
        f"{BASE_URL}/devices/{new_sn}/status",
        headers=headers,
        data=json.dumps(patch_body),
    )
    print_response("PATCH /devices/<serial_number>/status", r)

    # 6) PUT /devices/<serial_number> (sostituisce completamente le info)
    # Esempio: sostituiamo la camera con una bulb (full replacement)
    put_body = {
        "type": "bulb",
        "serial_number": new_sn,  # verrà comunque imposto dall'URL
        "brand": "IKEA",
        "room": "Bedroom",
        "installation_year": 2023,
        "status": "offline",
        "brightness_lumens": 1200,
        "color_capability": False
    }
    r = requests.put(
        f"{BASE_URL}/devices/{new_sn}",
        headers=headers,
        data=json.dumps(put_body),
    )
    print_response("PUT /devices/<serial_number>", r)

    # 7) GET /devices/<serial_number>/diagnostic/1.5 (stima diagnostica)
    r = requests.get(f"{BASE_URL}/devices/{new_sn}/diagnostic/1.5", headers=headers)
    print_response("GET /devices/<serial_number>/diagnostic/1.5", r)

    # 8) DELETE /devices/<serial_number> (elimina)
    r = requests.delete(f"{BASE_URL}/devices/{new_sn}", headers=headers)
    print_response("DELETE /devices/<serial_number>", r)

    # 9) GET /devices/<serial_number> (deve dare 404)
    r = requests.get(f"{BASE_URL}/devices/{new_sn}", headers=headers)
    print_response("GET /devices/<serial_number> (dopo delete)", r)
