import requests

import json

url_base = 'http://127.0.0.1:5000'

headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json'
}


def _print_response(response: requests.Response):
    print(f'\n Test: {response.request.method}'
          f'\nResponse:'
          f'\n http status code: {response.status_code}')
    #       f'\n json content:'
    #       )
    # print(json.dumps(response.json(), indent=4))
    try:
        print("JSON content:")
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    except ValueError:
        print("No JSON body. Raw text:")
        print(response.text)



def test_get():
    response = requests.get(
        url=f'{url_base}/',
        headers=headers
    )
    _print_response(response)

def test_get_bookings():
    response = requests.get(
        url=f'{url_base}/bookings',
        headers=headers
    )
    _print_response(response)

def test_get_booking_id(booking_id:str):
    response = requests.get(
        url=f'{url_base}/bookings/{booking_id}',
        headers = headers
    )
    _print_response(response)

def test_get_booking_wait(booking_id:str, factor:float) -> str:
    response = requests.get(
        url=f'{url_base}/bookings/{booking_id}/wait/{factor}',
        headers=headers
    ) 
    _print_response(response)

def test_post_booking(body: dict):
    response = requests.post(
        url=f'{url_base}/bookings',
        headers=headers,
        json=body
    )
    _print_response(response)

def test_put_booking(booking_id, body:dict)->str:
    response = requests.put(
        url=f'{url_base}/bookings/{booking_id}',
        headers=headers,
        json=body
    )
    _print_response(response)

def test_patch_booking(booking_id: str, body:dict)-> str:
    response = requests.patch(
        url=f'{url_base}/bookings/{booking_id}/status',
        headers=headers,
        json=body
    )
    _print_response(response)

def test_delete_booking(booking_id) -> str:
    response = requests.delete(
        url=f'{url_base}/bookings/{booking_id}',
        headers=headers
    )
    _print_response(response)

if __name__=='__main__':
    
    booking_id = "BK-3e67"
    factor = 1.0

    new = {
        "type": "exam",
        "booking_id": booking_id,
        "patient_name": "Giulia Verdi",
        "doctor": "Dr. Neri",
        "department": "Radiologia",
        "date": "2026-02-10",
        "time": "09:15",
        "status": "scheduled",
        "exam_type": "RMN",
        "requires_fasting": True
    }
    patch_body = {"status": "checked_in"}

    put_body = {
        "type": "visit",
        "booking_id": booking_id,
        "patient_name": "Giulia Verdi",
        "doctor": "Dr. Bianchi",
        "department": "Cardiologia",
        "date": "2026-02-12",
        "time": "11:00",
        "status": "scheduled",
        "visit_reason": "Dolore toracico",
        "first_time": True
    }

    test_get()
    test_get_bookings()

    test_post_booking(new)

    test_get_booking_id(booking_id)
    test_get_booking_wait(booking_id, factor)

    test_put_booking(booking_id, put_body)

    test_patch_booking(booking_id, patch_body)

    test_delete_booking(booking_id)
