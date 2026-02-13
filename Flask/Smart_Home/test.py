import requests
import json


url_base = 'http://127.0.0.1:5000'

headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json'
}

def _print_response(response: requests.Response) -> str:
    print(
        f'\nMetod: {response.request.method}'
        f'\n Response:'
        f'\n http status code: {response.status_code}'
    )
    try:
        print('json content: ')
        print(json.dumps(response.json(), indent=4))
    except ValueError:
        print('No json body')

def test_get()->str:
    response = requests.get(
        url=f'{url_base}',
        headers=headers
    )
    _print_response(response)

def test_get_devices()->str:
    response=requests.get(
        url=f'{url_base}/devices',
        headers=headers
    )
    _print_response(response)

def test_get_device(serial_number)->str:
    response = requests.get(
        url=f'{url_base}/devices/{serial_number}',
        headers=headers
    )
    _print_response(response)

def test_get_diagnostic(serial_number, factor):
    response = requests.get(
        url=f'{url_base}/devices/{serial_number}/diagnostic/{factor}',
        headers=headers
    )
    _print_response(response)

def test_post_device(body:dict)-> str:
    response = requests.post(
        url=f'{url_base}/devices',
        headers=headers,
        json=body
    )
    _print_response(response)

def test_put_device(serial_number, body):
    response = requests.put(
        url=f'{url_base}/devices/{serial_number}',
        headers=headers,
        json=body
    )
    _print_response(response)

def test_patch_devices(serial_number, body):
    response = requests.patch(
        url=f'{url_base}/devices/{serial_number}/status',
        headers=headers,
        json=body
    )
    _print_response(response)

def test_delete_device(serial_number):
    response = requests.delete(
        url=f'{url_base}/devices/{serial_number}',
        headers=headers
    )
    _print_response(response)


if __name__ == '__main__':

    serial_number = "SN-3e67"
    post_body = {
        "type": "camera",
        "serial_number": serial_number,
        "brand": "Philips",
        "room": "Living Room",
        "installation_year": 2022,
        "status": "online",
        "resolution": "4K",
        "night_vision": True
    }
    patch_body = {"status": "updating"}
    put_body = {
        "type": "bulb",
        "serial_number": serial_number,  
        "brand": "IKEA",
        "room": "Bedroom",
        "installation_year": 2023,
        "status": "offline",
        "brightness_lumens": 1200,
        "color_capability": False
    }

    test_get()
    test_get_devices()

    test_post_device(post_body)

    test_get_device(serial_number)

    test_get_diagnostic(serial_number, factor=1.1)

    test_put_device(serial_number, put_body)

    test_patch_devices(serial_number, patch_body)

    test_delete_device(serial_number)