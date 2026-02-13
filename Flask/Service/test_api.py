import requests
import json


BASE_URL = "http://localhost:5000"

headers = {
    "Content-type": "application/json",
    "Accept": "application/json"
}

def _show_response(response: requests.Response) -> None:
    line = '='*10
    print(f"\n\n{line} {response.request.method} {response.url} {line}")
    print(f"\nRESPONSE:\n"
          f"- HTTP Status Code: {response.status_code}\n"
          f"- JSON CONTENT:")
    print(json.dumps(response.json(), indent=4))

def test_get():
    response = requests.get(url=f"{BASE_URL}/", headers=headers)
    _show_response(response)

def test_get_devices():
    response = requests.get(url=f"{BASE_URL}/devices", headers=headers)
    _show_response(response)

def test_get_device_id(device_id:str):
    response = requests.get(url=f"{BASE_URL}/devices/{device_id}", headers=headers)
    _show_response(response)

def test_tempo_stimato(device_id:str, factor:float):
    response = requests.get(url=f"{BASE_URL}/devices/{device_id}/estimate/{factor}", headers=headers)
    _show_response(response)

def test_post_device(body:dict):
    response = requests.post(url=f"{BASE_URL}/devices", headers=headers,
                            json=body)
    response.encoding = 'utf-8'
    _show_response(response)

def test_put_device(device_id:str, body:dict):
    response = requests.put(url=f"{BASE_URL}/devices/{device_id}", headers=headers,
                            json=body)
    response.encoding = 'utf-8'
    _show_response(response)

def test_patch_status(device_id:str, body:dict):
    response = requests.patch(url=f"{BASE_URL}/devices/{device_id}/status", headers=headers,
                            json=body)
    response.encoding = 'utf-8'
    _show_response(response)

def test_delete_device(device_id:str,):
    response = requests.delete(url=f"{BASE_URL}/devices/{device_id}", headers=headers)
    response.encoding = 'utf-8'
    _show_response(response)

if __name__ == '__main__':
    # test_get()
    # test_get_devices()
    # test_get_device_id('t1')
    # test_tempo_stimato('t1', 1.5)


    body_post = {
        "device_type": "smartphone",
        "model": "Galaxy S21",
        "customer_name": "Mario Rossi",
        "purchase_year": 2021,
        "status": "received",
        "has_protective_case": True,
        "storage_gb": 128
    }

    body_patch_status = {
        "status": "repairing"
    }

    body_put_smartphone = {
        "device_type": "smartphone",
        "model": "Galaxy S21 Ultra",
        "customer_name": "Mario Rossi",
        "purchase_year": 2022,
        "status": "ready",
        "has_protective_case": False,
        "storage_gb": 256
    }

    body_put_laptop = {
        "device_type": "laptop",
        "model": "ThinkPad X1",
        "customer_name": "Mario Rossi",
        "purchase_year": 2020,
        "status": "diagnosing",
        "has_dedicated_gpu": True,
        "screen_size_inches": 14.0
    }


    test_post_device(body_post)
    test_get_devices()
    test_patch_status(2, body_patch_status)
    test_put_device(2, body_put_smartphone)



    