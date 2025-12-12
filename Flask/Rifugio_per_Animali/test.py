from classi import Dog

import requests

import json

url_base = "http://127.0.0.1:5000"

headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json'
}

def _print_response(response: requests.Response):
    linea:str = "=" * 10
    print(f"\n\n{linea} Test  -  {response.request.method}  {response.url} {linea}")
    print(f"\nRESPONSE:\n"
          f"- HTTP Status Code: {response.status_code}\n"
          f"- JSON CONTENT:")
    print(json.dumps(response.json(), indent=4)) 
    # response.json() -> converte la risposta JSON in un oggetto Python
    # json.dumps(..., indent=4) -> riconverte in stringa formattata come dizionario:


 # response è un oggetto di tipo requests.Response

    # response.request.method    GET / POST
    # response.url               URL chiamato
    # response.status_code       200 / 404 / 400
    # response.json()            dati restituiti

def test_get_info() -> str:
    response = requests.get(
        url = f"{url_base}/",
        headers = headers
    )
    _print_response(response)

def test_get_animals() -> str:
    response = requests.get(       
        url = f"{url_base}/animals",
        headers = headers
    )
    _print_response(response)

def test_get_animal_id(animal_id:str) -> str:
    response = requests.get(
        url = f"{url_base}/animals/{animal_id}",
        headers = headers
    )
    _print_response(response)

def test_get_animal_food(animal_id:str) -> str:
    response = requests.get(
        url = f"{url_base}/animals/{animal_id}/food",
        headers = headers
    )
    _print_response(response)

def test_get_animal_adoption(animal_id:str) -> str:
    response = requests.get(
        url = f"{url_base}/animals/{animal_id}/adoption",
        headers = headers
    )
    _print_response(response)


def test_post_animals(playload:dict) -> str:
    response = requests.post(
        url = f"{url_base}/animals/add",
        headers = headers,
        json = playload
    )
    _print_response(response)


def test_post_animal_adoption(animal_id:str, adopter_name:str) -> str:
    response = requests.post(
        url = f"{url_base}/animals/{animal_id}/adopt",
        headers = headers,
        json = {"animal_id": animal_id, "adopter_name": adopter_name}
    )
    _print_response(response)


if __name__ == "__main__":

    test_get_info()
    test_get_animals()
    test_get_animal_id("d1")
    test_get_animal_food("c1")
    test_get_animal_adoption("d1")
    
    rem:dict = {
        "type": "dog",
        "id":"d2", 
        "name": "Rem", 
        "age_years": 2, 
        "weight_kg": 35.0, 
        "breed": "Staf", 
        "is_trained": True
        }
    
    test_post_animals(rem)

    test_post_animal_adoption("d1", "Nat")