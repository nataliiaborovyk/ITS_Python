
# from __future__ import annotations
from abc import ABC, abstractmethod

class Animal(ABC):

    id: str
    name: str
    age_years: int
    weight_kg: float

    def __init__(self, id:str, name:str, age_years:int, weight_kg:float) -> None:
        self.id = id
        self.name = name
        self.age_years = age_years
        self.weight_kg = weight_kg

    @abstractmethod
    def species(self) -> str:
        pass

    @abstractmethod
    def daily_food_grams(self) -> int:
        pass

    def info(self) -> dict[str, str|int|float|bool]:
        diz: dict[str, str|int|float|bool] = {
            "id": self.id,
            "name": self.name,
            "species": self.species(),
            "age_years": self.age_years,
            "weight_kg": self.weight_kg
        }        
        return diz
    
    def bmi_like(self) -> float:
        result: float = self.weight_kg / (self.age_years + 1)
        return result
    
    def _get_id(self) -> str:
        return self.id

class Dog(Animal):

    breed: str
    is_trained: bool

    def __init__(self, *, id:str, name:str, age_years:int, weight_kg:float, 
                 breed:str, is_trained:bool) -> None:
        super().__init__(id, name, age_years, weight_kg)
        self.breed = breed
        self.is_trained = is_trained

    def species(self) -> str:
        return "dog"
    
    def daily_food_grams(self) -> int:
        result: int = 200 + self.age_years * 50
        return result
    
    def info(self) -> dict[str, str|int|float|bool]:
        da_animal: dict[str, str|int|float|bool] = super().info()
        da_animal["breed"] = self.breed
        da_animal["is_trained"] = self.is_trained
        return da_animal

    
class Cat(Animal):

    indoor_only: bool
    favorite_toy: str

    def __init__(self, *, id:str, name:str, age_years:int, weight_kg:float, 
                 indoor_only: bool, favorite_toy: str) -> None:
        super().__init__(id, name, age_years, weight_kg)
        self.indoor_only = indoor_only
        self.favorite_toy = favorite_toy

    def species(self) -> str:
        return "cat"

    def daily_food_grams(self) -> int:
        result: int = 100 + self.age_years * 30
        return result 

    def info(self) -> dict[str, str|int|float|bool]:
        da_animal: dict[str, str|int|float|bool] = super().info()
        da_animal["indoor_only"] = self.indoor_only
        da_animal["favorite_toy"] = self.favorite_toy
        return da_animal
    
class Shelter:

    animals: dict[str, Animal]
    adoptions: dict[str, str]

    def __init__(self, animals: dict[str, Animal]|None = None, 
                 adoptions: dict[str, str]|None = None)  -> None:
        self.animals = animals or {}
        self.adoptions = adoptions or {}

    def add(self, animal: Animal) -> None:
        if animal._get_id() in self.animals:
            raise KeyError("Animale gia presente")
        self.animals[animal._get_id()] = animal

    def get_animal_id(self, animal_id: str) -> Animal|None:
        if animal_id not in self.animals:
            # raise KeyError(f"Animane con id {animal_id} non è presente")
            return None
        return self.animals[animal_id]
    
    def list_all(self) -> list[dict[str,dict[str|int|float|bool]]]:
        result = []
        for k, v in self.animals.items():
            val: dict = {k: v.info()}
            result.append(val)
        return result
        # return [a.info() for a in self.animals.values()]
        

    
    def is_adopted(self, animal_id:str) -> bool:
        if animal_id in self.adoptions:
            return True
        return False
    
    def set_adopted(self, *, animal_id:str, adopter_name: str) -> None:
        if animal_id in self.adoptions:
            raise KeyError(f"Animale con id {animal_id} è gia stato adottato")
        self.adoptions[animal_id] = adopter_name

    def get_adopter_name(self, animal_id:str) -> str:
        if animal_id not in self.adoptions:
            raise KeyError(f"Animale con id {animal_id} non è adottato")
        return self.adoptions[animal_id]

    
    


rifugio: Shelter = Shelter()

lilu: Dog = Dog(id="d1", name="Lilu", age_years=5, weight_kg=25.0, breed="Choa-Choa", is_trained=True)
asia: Cat = Cat(id="c1", name="Asia", age_years=11, weight_kg=5.5, indoor_only=True, favorite_toy="filo qualsiasi")

rifugio.add(lilu)
rifugio.add(asia)


    

if __name__ == "__main__":

    print(lilu.info())
    print(rifugio.list_all())




