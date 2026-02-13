import requests

url_base: str = 'http://127.0.0.1:5000'

headers = {
    'Content-type':'application/json',
    'Accept':'application/json'
}

# GET /
response = requests.get(
    url=f'{url_base}/',
    headers=headers
)
print('GET /', response.json())

# GET /bookings
response = requests.get(
    url=f'{url_base}/bookings',
    headers=headers
)
print('GET /bookings', response.json())

# POST /bookings
booking_id = "BK-3e67"
new = {
    'type':'exam',
    'booking_id':booking_id,
    "patient_name": "Giulia Verdi",
    "doctor": "Dr. Neri",
    "department": "Radiologia",
    "date": "2026-02-10",
    "time": "09:15",
    "status": "scheduled",
    "exam_type": "RMN",
    "requires_fasting": True
}
response = requests.post(
    url=f'{url_base}/bookings',
    headers=headers,
    json=new
)
print('POST /bookings', response.json())

# GET /bookings/<booking_id>
booking_id = "BK-3e67"
response = requests.get(
    url=f'{url_base}/bookings/{booking_id}',
    headers=headers
)
print('GET /bookings/<booking_id>', response.json())

# GET /bookings/<booking_id>/wait/<factor>
factor = 1.0
response = requests.get(
    url=f'{url_base}/bookings/{booking_id}/wait/{factor}',
    headers=headers
)
print('GET /bookings/<booking_id>/wait/<factor>', response.json())

# PUT /bookings/<booking_id>
body_put = {
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
response = requests.put(
    url=f'{url_base}/bookings/{booking_id}',
    headers=headers,
    json=body_put
)
print('PUT /bookings/<booking_id>', response.json())

# PATCH /bookings/<booking_id>/status
body_patch = {
    'status': 'checked_in'
}
response = requests.patch(
    url=f'{url_base}/bookings/{booking_id}/status',
    headers=headers,
    json=body_patch
)
print('PATCH /bookings/<booking_id>/status', response.json())

# DELETE /bookings/<booking_id>
response = requests.delete(
    url=f'{url_base}/bookings/{booking_id}',
    headers=headers
)
print('DELETE /bookings/<booking_id>', response.json())