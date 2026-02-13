import json
import requests

# Assumiamo che l'app Flask di shelter.py giri su questa base URL
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

    # 2) GET /animals (lista iniziale: d1 e c1)
    r = requests.get(f"{BASE_URL}/animals", headers=headers)
    print_response("GET /animals (lista iniziale)", r)

    # 3) GET /animals/d1 (dettagli del cane di esempio)
    r = requests.get(f"{BASE_URL}/animals/d1", headers=headers)
    print_response("GET /animals/d1", r)

    # 4) GET /animals/d1/food (cibo giornaliero)
    r = requests.get(f"{BASE_URL}/animals/d1/food", headers=headers)
    print_response("GET /animals/d1/food", r)

    # 5) GET /animals/d1/adoption (stato di adozione iniziale, atteso False)
    r = requests.get(f"{BASE_URL}/animals/d1/adoption", headers=headers)
    print_response("GET /animals/d1/adoption (prima dell'adozione)", r)

    # 6) POST /animals/add - aggiungiamo un nuovo cane d2
    new_dog_id = "d2"
    new_dog = {
        "type": "dog",
        "id": new_dog_id,
        "name": "Fido",
        "age_years": 1,
        "weight_kg": 10.0,
        "breed": "beagle",
        "is_trained": False
    }
    r = requests.post(
        f"{BASE_URL}/animals/add",
        headers=headers,
        data=json.dumps(new_dog),
    )
    print_response("POST /animals/add (nuovo cane d2)", r)

    # 7) POST /animals/add - aggiungiamo un nuovo gatto c2
    new_cat_id = "c2"
    new_cat = {
        "type": "cat",
        "id": new_cat_id,
        "name": "Pallina",
        "age_years": 2,
        "weight_kg": 3.5,
        "indoor_only": True,
        "favorite_toy": "mouse"
    }
    r = requests.post(
        f"{BASE_URL}/animals/add",
        headers=headers,
        data=json.dumps(new_cat),
    )
    print_response("POST /animals/add (nuovo gatto c2)", r)

    # 8) GET /animals (lista dopo le aggiunte)
    r = requests.get(f"{BASE_URL}/animals", headers=headers)
    print_response("GET /animals (dopo aggiunta d2 e c2)", r)

    # 9) GET /animals/d2 (controlliamo che il cane sia stato aggiunto)
    r = requests.get(f"{BASE_URL}/animals/{new_dog_id}", headers=headers)
    print_response(f"GET /animals/{new_dog_id}", r)

    # 10) POST /animals/d2/adopt (adottiamo il cane d2)
    adopt_body = {
        "adopter_name": "Mario Rossi"
    }
    r = requests.post(
        f"{BASE_URL}/animals/{new_dog_id}/adopt",
        headers=headers,
        data=json.dumps(adopt_body),
    )
    print_response(f"POST /animals/{new_dog_id}/adopt", r)

    # 11) GET /animals/d2/adoption (ora dovrebbe risultare adottato)
    r = requests.get(f"{BASE_URL}/animals/{new_dog_id}/adoption", headers=headers)
    print_response(f"GET /animals/{new_dog_id}/adoption (dopo adozione)", r)

    # 12) POST /animals/d2/adopt di nuovo (dovrebbe dare errore "already adopted")
    r = requests.post(
        f"{BASE_URL}/animals/{new_dog_id}/adopt",
        headers=headers,
        data=json.dumps(adopt_body),
    )
    print_response(f"POST /animals/{new_dog_id}/adopt (seconda volta, errore atteso)", r)

    # 13) GET /animals/xyz (animale inesistente, ci aspettiamo 404)
    r = requests.get(f"{BASE_URL}/animals/xyz", headers=headers)
    print_response("GET /animals/xyz (inesistente)", r)

    # 14) POST /animals/add con id duplicato (ad es. d1), errore 400 atteso
    duplicate_dog = {
        "type": "dog",
        "id": "d1",  # già usato dal cane iniziale
        "name": "AltroCane",
        "age_years": 4,
        "weight_kg": 20.0,
        "breed": "labrador",
        "is_trained": True
    }
    r = requests.post(
        f"{BASE_URL}/animals/add",
        headers=headers,
        data=json.dumps(duplicate_dog),
    )
    print_response("POST /animals/add (id duplicato d1, errore atteso)", r)


if __name__ == "__main__":
    main()
