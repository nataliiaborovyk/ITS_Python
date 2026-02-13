from abc import ABC, abstractmethod
from flask import Flask, jsonify, request, url_for

# ==========================
# Classi di dominio
# ==========================

class Animal(ABC):
    def __init__(self, animal_id: str, name: str, age_years: int, weight_kg: float):
        self.id = animal_id
        self.name = name
        self.age_years = age_years
        self.weight_kg = weight_kg

    @abstractmethod
    def species(self) -> str:
        """Specie dell'animale (dog, cat, ...)"""
        pass

    @abstractmethod
    def daily_food_grams(self) -> int:
        """Quantità di cibo giornaliera in grammi."""
        pass

    def bmi_like(self) -> float:
        """Indice fittizio di forma fisica."""
        return self.weight_kg / (self.age_years + 1)

    def info(self) -> dict:
        """Informazioni di base + eventuali attributi specifici nelle sottoclassi."""
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species(),
            "age_years": self.age_years,
            "weight_kg": self.weight_kg,
            "bmi_like": self.bmi_like(),
        }


class Dog(Animal):
    def __init__(self, animal_id: str, name: str, age_years: int, weight_kg: float,
                 breed: str, is_trained: bool):
        super().__init__(animal_id, name, age_years, weight_kg)
        self.breed = breed
        self.is_trained = is_trained

    def species(self) -> str:
        return "dog"

    def daily_food_grams(self) -> int:
        # Formula semplice e "plausibile"
        return 200 + self.age_years * 50

    def info(self) -> dict:
        base = super().info()
        base["breed"] = self.breed
        base["is_trained"] = self.is_trained
        return base


class Cat(Animal):
    def __init__(self, animal_id: str, name: str, age_years: int, weight_kg: float,
                 indoor_only: bool, favorite_toy: str):
        super().__init__(animal_id, name, age_years, weight_kg)
        self.indoor_only = indoor_only
        self.favorite_toy = favorite_toy

    def species(self) -> str:
        return "cat"

    def daily_food_grams(self) -> int:
        # Anche qui una formula inventata ma coerente
        return 100 + self.age_years * 30

    def info(self) -> dict:
        base = super().info()
        base["indoor_only"] = self.indoor_only
        base["favorite_toy"] = self.favorite_toy
        return base


class Shelter:
    def __init__(self):
        self.animals: dict[str, Animal] = {}
        # adoptions: id -> nome adottante
        self.adoptions: dict[str, str] = {}

    def add(self, animal: Animal) -> bool:
        """Aggiunge un animale. Ritorna False se l'id esiste già."""
        if animal.id in self.animals:
            return False
        self.animals[animal.id] = animal
        return True

    def get(self, animal_id: str) -> Animal | None:
        return self.animals.get(animal_id)

    def list_all(self) -> list[Animal]:
        return list(self.animals.values())

    def is_adopted(self, animal_id: str) -> bool:
        return animal_id in self.adoptions

    def set_adopted(self, animal_id: str, adopter_name: str) -> None:
        self.adoptions[animal_id] = adopter_name

    def get_adopter(self, animal_id: str) -> str | None:
        return self.adoptions.get(animal_id)


# ==========================
# Inizializzazione dati
# ==========================

shelter = Shelter()

# Aggiungiamo un cane e un gatto di esempio
dog1 = Dog(animal_id="d1", name="Rex", age_years=2, weight_kg=18.5,
           breed="border collie", is_trained=True)
cat1 = Cat(animal_id="c1", name="Micia", age_years=3, weight_kg=4.2,
           indoor_only=True, favorite_toy="ball")

shelter.add(dog1)
shelter.add(cat1)

# ==========================
# Applicazione Flask
# ==========================

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """Pagina principale, con messaggio e link alle altre route."""
    sample_dog_id = "d1"
    return jsonify({
        "message": "Welcome to Animal Shelter API",
        "links": {
            "list_animals": url_for("list_animals"),
            "sample_dog_details": url_for("get_animal", animal_id=sample_dog_id),
            "sample_dog_food": url_for("get_food", animal_id=sample_dog_id),
            "sample_dog_adoption": url_for("get_adoption", animal_id=sample_dog_id),
            "add_animal": url_for("add_animal"),
        }
    })


@app.route("/animals", methods=["GET"])
def list_animals():
    """Restituisce la lista di tutti gli animali nel rifugio."""
    animals_info = [animal.info() for animal in shelter.list_all()]
    return jsonify(animals_info)


@app.route("/animals/<animal_id>", methods=["GET"])
def get_animal(animal_id):
    """Restituisce i dettagli di un singolo animale."""
    animal = shelter.get(animal_id)
    if not animal:
        return jsonify({"error": "Animal not found"}), 404
    return jsonify(animal.info())


@app.route("/animals/<animal_id>/food", methods=["GET"])
def get_food(animal_id):
    """Restituisce il cibo giornaliero consigliato per l'animale."""
    animal = shelter.get(animal_id)
    if not animal:
        return jsonify({"error": "Animal not found"}), 404
    return jsonify({
        "id": animal.id,
        "name": animal.name,
        "species": animal.species(),
        "daily_food_grams": animal.daily_food_grams()
    })


@app.route("/animals/<animal_id>/adoption", methods=["GET"])
def get_adoption(animal_id):
    """Restituisce lo stato di adozione dell'animale."""
    animal = shelter.get(animal_id)
    if not animal:
        return jsonify({"error": "Animal not found"}), 404

    if shelter.is_adopted(animal_id):
        adopter = shelter.get_adopter(animal_id)
        return jsonify({
            "id": animal.id,
            "adopted": True,
            "adopter_name": adopter
        })
    else:
        return jsonify({
            "id": animal.id,
            "adopted": False
        })


@app.route("/animals/add", methods=["POST"])
def add_animal():
    """
    Aggiunge un nuovo animale.
    Body JSON richiesto:
    - type: "dog" o "cat"
    - campi comuni: id, name, age_years, weight_kg
    - per dog: breed, is_trained
    - per cat: indoor_only, favorite_toy
    """
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    animal_type = data.get("type")
    animal_id = data.get("id")
    name = data.get("name")
    age_years = data.get("age_years")
    weight_kg = data.get("weight_kg")

    if not all([animal_type, animal_id, name]) or age_years is None or weight_kg is None:
        return jsonify({"error": "Missing required fields"}), 400

    if shelter.get(animal_id) is not None:
        return jsonify({"error": "Animal with this id already exists"}), 400

    try:
        age_years = int(age_years)
        weight_kg = float(weight_kg)
    except ValueError:
        return jsonify({"error": "age_years must be int, weight_kg must be float"}), 400

    if animal_type == "dog":
        breed = data.get("breed")
        is_trained = data.get("is_trained")
        if breed is None or is_trained is None:
            return jsonify({"error": "Missing fields for dog: breed, is_trained"}), 400
        animal = Dog(animal_id=animal_id, name=name, age_years=age_years,
                     weight_kg=weight_kg, breed=breed, is_trained=bool(is_trained))

    elif animal_type == "cat":
        indoor_only = data.get("indoor_only")
        favorite_toy = data.get("favorite_toy")
        if indoor_only is None or favorite_toy is None:
            return jsonify({"error": "Missing fields for cat: indoor_only, favorite_toy"}), 400
        animal = Cat(animal_id=animal_id, name=name, age_years=age_years,
                     weight_kg=weight_kg, indoor_only=bool(indoor_only),
                     favorite_toy=favorite_toy)
    else:
        return jsonify({"error": "Unknown animal type, expected 'dog' or 'cat'"}), 400

    shelter.add(animal)
    return jsonify({
        "status": "ok",
        "added": animal.info()
    }), 201


@app.route("/animals/<animal_id>/adopt", methods=["POST"])
def adopt_animal(animal_id):
    """
    Registra l'adozione di un animale.
    Body JSON:
    {
        "adopter_name": "Mario Rossi"
    }
    """
    animal = shelter.get(animal_id)
    if not animal:
        return jsonify({"error": "Animal not found"}), 404

    if shelter.is_adopted(animal_id):
        return jsonify({"error": "Animal already adopted"}), 400

    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    adopter_name = data.get("adopter_name")
    if not adopter_name:
        return jsonify({"error": "Missing adopter_name"}), 400

    shelter.set_adopted(animal_id, adopter_name)

    return jsonify({
        "id": animal.id,
        "adopted": True,
        "adopter_name": adopter_name
    }), 200


if __name__ == "__main__":
    # Avvia il server in debug sulla porta 5000
    app.run(debug=True, host="127.0.0.1", port=5000)
