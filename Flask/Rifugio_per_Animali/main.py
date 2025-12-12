from classi import Cat, Dog, rifugio, Animal #, Shelter,  lilu, asia

from flask import Flask, url_for, jsonify, request

app = Flask(__name__)
# app.config["JSON_SORT_KEYS"] = False    # se voglio che prima stampa "messaggio" poi "link" (non ordinera in alfabetico)

# GET


# 2. GET /animals
# Restituisce un JSON con la lista degli animali presenti nel rifugio.
# Ogni elemento della lista può essere:  una stringa descrittiva, ad esempio  "d1 - Rex (dog) - 2 years - 18.5kg",
#     oppure  un dizionario con i campi principali dell’animale (quelli restituiti da info()).
# La scelta è libera, ma deve essere coerente in tutto il programma (se scegli la rappresentazione come dizionario, usala ovunque per le liste).

@app.route("/animals", methods = ['GET']) 
def get_animals():
    return jsonify(rifugio.list_all())



# 3. GET /animals/<animal_id>
# Restituisce un JSON con un solo elemento che rappresenta i dettagli dell’animale con l’ID specificato.
# Ad esempio:
# { "id": "d1", "name": "Rex", "species": "dog", "age_years": 2, "weight_kg": 18.5, "breed": "border collie", "is_trained": true }
# Se l’animale non esiste, la route dovrebbe restituire un JSON di errore (es. {"error": "Animal not found"}) con status code appropriato (ad esempio 404).

@app.route("/animals/<string:animal_id>", methods = ['GET'])
def get_animal_id(animal_id:str) -> dict|str:
    animal: Animal | None = rifugio.get_animal_id(animal_id)

    if animal is None:
        return jsonify({"errore": "Animale con id indicato non è presente"}), 404
    return jsonify(animal.info()), 200




# 4. GET /animals/<animal_id>/food
# Restituisce un JSON con le informazioni sul cibo giornaliero stimato per l’animale specificato.
# L’output può essere, ad esempio:  { "id": "d1", "daily_food_grams": 350 }
# oppure una struttura più ricca a tua scelta, purché sia JSON.
# Anche qui, se l’animale non esiste, va gestito l’errore.
@app.route("/animals/<string:animal_id>/food", methods=['GET'])
def get_food(animal_id:str) -> dict:
    animal: Animal | None = rifugio.get_animal_id(animal_id)

    if animal is None:
        return jsonify({"errore": "Animale con id indicato non è presente"}), 404
    diz: dict = {
        "id": animal_id, 
        "daily_food_grams": animal.daily_food_grams() 
        }
    return jsonify(diz), 200



# 5. GET /animals/<animal_id>/adoption
# Restituisce lo stato di adozione dell’animale specificato.
# Esempi di output:
# Animale non adottato:  { "id": "d1", "adopted": false }
# Animale adottato: { "id": "d1", "adopted": true, "adopter_name": "Mario Rossi" }

@app.route("/animals/<string:animal_id>/adoption", methods=['GET'])
def get_animals_adoption(animal_id: str) -> dict:
    animal: Animal | None = rifugio.get_animal_id(animal_id)

    if animal is None :
        return jsonify({"errore": "Animale con id indicato non è presente nel rifugio"}), 404
    if not rifugio.is_adopted(animal_id):
        diz:dict = {
             "id": animal_id, 
             "adopted": False 
             }
        return jsonify(diz), 200
    diz: dict = {
        "id": animal_id, 
        "adopted": True, 
        "adopter_name": rifugio.get_adopter_name(animal_id)
        }
    return jsonify(diz), 200


# 1. GET /
# Restituisce un JSON con:
#     una breve descrizione del servizio, ad esempio:     { "message": "Welcome to Animal Shelter API" }
#     alcuni link testuali che indicano le altre route disponibili, ad esempio:
#         /animals
#         /animals/d1
#         /animals/d1/food
#         /animals/d1/adoption
#     Questi link devono essere generati dinamicamente con url_for() e poi inseriti nel JSON, ad esempio:
#     { "message": "...",
#        "links": { "list_animals": url_for("list_animals"), "sample_dog": url_for("get_animal", animal_id="d1"), ... } }

@app.route("/")
def info():
    result = {
        "message": "Welcome to Animal Shelter API",
        "links": {
            "list_animals": {
                "url": url_for("get_animals"), 
                "method": "GET"
                },
            "get_animal": {
                "url": url_for("get_animal_id", animal_id="animal_id"), 
                "method": "GET"
                },
            "get_food": {
                "url": url_for("get_food", animal_id="animal_id"), 
                "method": "GET"
                },
            "get_adoptions": {
                "url": url_for("get_animals_adoption", animal_id="animal_id"), 
                "method": "GET"
                },
            "post_animal": {
                "url": url_for("post_animals"),
                "method": "POST"
            },
            "post_animals_adoption": {
                "url": url_for("post_animals_adoption", animal_id="animal_id"),
                "method": "POST"               
            }
        }
    }
    return jsonify(result), 200


# POST

# 1. POST /animals/add
# Permette di aggiungere un nuovo animale al rifugio.
# Il body JSON deve contenere le informazioni necessarie per creare l’animale e un campo che specifica il tipo, ad esempio "dog" o "cat".
# Esempio per un cane:
# { "type": "dog", "id": "d3", "name": "Rex", "age_years": 2, "weight_kg": 18.5, "breed": "border collie", "is_trained": true }
# Esempio per un gatto:
# { "type": "cat", "id": "c5", "name": "Micia", "age_years": 3, "weight_kg": 4.2, "indoor_only": true, "favorite_toy": "ball" }
# La funzione della route deve:
#     leggere il JSON dalla richiesta;
#     verificare che il campo "type" sia presente e valido ("dog" o "cat");
#     controllare che i campi richiesti (id, name, ecc.) siano presenti;
#     creare l’istanza della sottoclasse corretta (Dog o Cat);
#     aggiungere l’animale al Shelter con shelter.add(...);
#     restituire un JSON di conferma, ad esempio:
#     { "status": "ok", "added": { "id": "d3", "species": "dog" } }
# In caso di errore (id già esistente, campi mancanti, tipo non riconosciuto) deve restituire un JSON di errore con uno status code adeguato (es. 400 Bad Request).

@app.route("/animals/add", methods=['POST'])
def post_animals() -> dict:
    data: dict = request.get_json()

    if "type" not in data:
        return jsonify({"errore": "Per creare un animale, fornire il tipo"}), 400
    elif "id" not in data:
         return jsonify({"errore": "Per creare un animale, fornire il id"}), 400     
    elif "name" not in data:
        return jsonify({"errore": "Per creare un animale, fornire il name"}), 400
    elif "age_years" not in data:
        return jsonify({"errore": "Per creare un animale, fornire il age_years"}), 400
    elif "weight_kg" not in data:
        return jsonify({"errore": "Per creare un animale, fornire il weight_kg"}), 400  
    elif rifugio.get_animal_id(data["id"]) is not None:
        return jsonify({"errore": "Animale con id indicato è gia presente nel rifugio"}), 409


    if data["type"] == "dog":
        if "breed" not in data:
            return jsonify({"errore": "Per creare un cane, fornire il breed"}), 400
        elif "is_trained" not in data:
            return jsonify({"errore": "Per creare un cane, fornire il is_trained"}), 400
        animale: Dog = Dog(
            id=data["id"],
            name=data["name"],
            age_years=data["age_years"],
            weight_kg=data["weight_kg"],
            breed=data["breed"],
            is_trained=data["is_trained"]
        )
    elif data["type"] == "cat":
        if "indoor_only" not in data:
            return jsonify({"errore": "Per creare un gatto, fornire il indoor_only"}), 400
        elif "favorite_toy" not in data:
            return jsonify({"errore": "Per creare un gatto, fornire il favorite_toy"}), 400
        animale: Cat = Cat(
            id=data["id"],
            name=data["name"],
            age_years=data["age_years"],
            weight_kg=data["weight_kg"],
            indoor_only=data["indoor_only"],
            favorite_toy=data["favorite_toy"]
        ) 
    else: 
        return jsonify({"errore": "Per creare un animale, fornire il tipo \"dog\" o \"cat\""}), 400  
       
    rifugio.add(animale)
    return jsonify({ "status": "ok", "added": { "id": animale._get_id(), "species": animale.species() } }), 200



# 2. POST /animals/<animal_id>/adopt
# Registra l’adozione di un animale.
# Il body JSON deve contenere almeno il nome dell’adottante, ad esempio:
# { "adopter_name": "Mario Rossi" }
# La funzione della route deve:
#     verificare che l’animale con id animal_id esista nel rifugio;
#     leggere il nome dell’adottante dal JSON;
#     aggiornare la struttura di adozioni del Shelter (ad esempio con shelter.set_adopted(animal_id, adopter_name));
#     restituire un JSON di conferma, ad esempio:
#     { "id": "d1", "adopted": true, "adopter_name": "Mario Rossi" }
# Se l’animale non esiste, oppure è già adottato (se vuoi gestire anche questo caso), la route deve restituire un JSON di errore e uno status code appropriato (es. 404 o 400).


@app.route("/animals/<string:animal_id>/adopt", methods=['POST'])
def post_animals_adoption(animal_id:str) -> dict:
    data:dict = request.get_json()

    if "adopter_name" not in data:
        return jsonify({"errore": "Per adottare animale fornire il adopter_name"}), 400
    elif rifugio.get_animal_id(animal_id) is None:
        return jsonify({"errore": "Animale con id fornito non è presente"}), 404
    elif rifugio.is_adopted(animal_id):
        return jsonify({"errore": "Animale con id fornito è gia stato adottato"}), 409 
      
    rifugio.set_adopted(animal_id=animal_id, adopter_name=data["adopter_name"])
    return jsonify({ "id": animal_id, "adopted": True, "adopter_name": data["adopter_name"] })




