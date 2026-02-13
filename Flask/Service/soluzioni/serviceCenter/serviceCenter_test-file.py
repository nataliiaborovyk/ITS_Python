import json
import requests

BASE_URL = "http://127.0.0.1:5000"


def print_response(title, response):
    print(f"=== {title} ===")
    print("Status code:", response.status_code)
    try:
        data = response.json()
        print("JSON response:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except ValueError:
        print("Raw response:")
        print(response.text)
    print("=" * 40)


def main():
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # 1) GET /
    r = requests.get(f"{BASE_URL}/", headers=headers)
    print_response("GET /", r)

    # 2) GET /devices
    r = requests.get(f"{BASE_URL}/devices", headers=headers)
    print_response("GET /devices", r)

    # 3) POST /devices - creiamo un nuovo smartphone
    new_device_id = "d100"
    new_device = {
        "type": "smartphone",
        "id": new_device_id,
        "model": "Galaxy S21",
        "customer_name": "Mario Rossi",
        "purchase_year": 2021,
        "status": "received",
        "has_protective_case": True,
        "storage_gb": 256,
    }
    r = requests.post(
        f"{BASE_URL}/devices",
        headers=headers,
        data=json.dumps(new_device),
    )
    print_response("POST /devices (create smartphone)", r)

    # 4) GET /devices/<new_device_id>
    r = requests.get(f"{BASE_URL}/devices/{new_device_id}", headers=headers)
    print_response(f"GET /devices/{new_device_id}", r)

    # 5) GET /devices/<new_device_id>/estimate/1.5
    r = requests.get(
        f"{BASE_URL}/devices/{new_device_id}/estimate/1.5",
        headers=headers,
    )
    print_response(f"GET /devices/{new_device_id}/estimate/1.5", r)

    # 6) PATCH /devices/<new_device_id>/status
    patch_body = {
        "status": "repairing"
    }
    r = requests.patch(
        f"{BASE_URL}/devices/{new_device_id}/status",
        headers=headers,
        data=json.dumps(patch_body),
    )
    print_response(f"PATCH /devices/{new_device_id}/status", r)

    # 7) PUT /devices/<new_device_id> - lo trasformiamo in un laptop
    put_body = {
        "type": "laptop",
        "model": "Dell XPS 15",
        "customer_name": "Mario Rossi",
        "purchase_year": 2020,
        "status": "diagnosing",
        "has_dedicated_gpu": True,
        "screen_size_inches": 15.6,
    }
    r = requests.put(
        f"{BASE_URL}/devices/{new_device_id}",
        headers=headers,
        data=json.dumps(put_body),
    )
    print_response(f"PUT /devices/{new_device_id}", r)

    # 8) GET /devices/<new_device_id> dopo il PUT
    r = requests.get(f"{BASE_URL}/devices/{new_device_id}", headers=headers)
    print_response(f"GET /devices/{new_device_id} (after PUT)", r)

    # 9) DELETE /devices/<new_device_id>
    r = requests.delete(
        f"{BASE_URL}/devices/{new_device_id}",
        headers=headers,
    )
    print_response(f"DELETE /devices/{new_device_id}", r)

    # 10) GET /devices/<new_device_id> dopo il DELETE (ci aspettiamo 404)
    r = requests.get(f"{BASE_URL}/devices/{new_device_id}", headers=headers)
    print_response(f"GET /devices/{new_device_id} (after DELETE)", r)


if __name__ == "__main__":
    main()
