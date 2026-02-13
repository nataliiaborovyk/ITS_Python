from abc import ABC, abstractmethod
from Index import Index
from typing import TYPE_CHECKING, Any, Self


class Veichle(ABC):

    _index_id: Index[str, Self] = Index('Veichle') 

    def __init__(self, *, id_targa: str, model:str, driver_name:str, registration_year:int, status:str) -> None:
        self.id = None
        self._set_id(id_targa)
        self.model = model
        self.driver_name = driver_name
        self.registration_year = registration_year
        self.status = status

    @abstractmethod
    def vehicle_type(self):
        pass

    @abstractmethod
    def base_cleaning_time(self):
        pass

    @abstractmethod
    def wear_level(self):
        pass

    def _set_id(self, targa:str) -> None:
        targa = targa.strip().upper()
        if targa == "":
            raise ValueError("Il targa non puo essere vuota")
        altra_targa = self._index_id.get(targa)
        if altra_targa is not None and altra_targa is not self:
            raise ValueError("Il targa è gia usato")
        if self.id is not None:
            self._index_id.remove(self.id)
        self.id = targa
        self._index_id.add(targa, self)

    def get_id(self) -> str:
        return self.id
    
    def get_model(self) -> str:
        return self.model
    
    def get_driver_name(self) -> str:
        return self.driver_name
    
    def get_registration_year(self) -> int:
        return self.registration_year
    
    def get_status(self) -> str:
        return self.status
    
    def set_status(self, new_status:str) -> None:
        self.status = new_status
 
    def info(self) -> dict:
        return {
            "id": self.get_id(),
            "model": self.get_model(),
            "driver_name": self.get_driver_name(),
            "veichle_type": self.vehicle_type(),
            "registration_year": self.get_registration_year(),
            "status": self.get_status()
        }
        
    def estimated_prep_time(self, factor: float = 1.0) -> int:
        return int(self.base_cleaning_time() * factor + self.wear_level()*15)




class Car(Veichle):

    def __init__(self, *, id_targa: str, model:str, driver_name:str, registration_year:int, status:str,
                 doors:int, is_cabrio:bool) -> None:
        super().__init__(id_targa=id_targa, model=model, driver_name=driver_name, 
                         registration_year=registration_year, status=status)
        self.doors = doors
        self.is_cabrio = is_cabrio

    def vehicle_type(self):
        return 'car'
    
    def base_cleaning_time(self):
        return 30
    
    def wear_level(self):
        return 1
    
    def get_doors(self) -> int:
        return self.doors
    
    def get_is_cabrio(self) -> bool:
        return self.is_cabrio
    
    def info(self) -> None:
        dict_info: dict = super().info()
        dict_info['doors'] = self.get_doors()
        dict_info['is_cabrio'] = self.get_is_cabrio()
        return dict_info

class Van(Veichle):

    def __init__(self, *, id_targa: str, model:str, driver_name:str, registration_year:int, status:str,
                 max_load_kg:int, require_special_license:bool) -> None:
        super().__init__(id_targa=id_targa, model=model, driver_name=driver_name, 
                         registration_year=registration_year, status=status)
        self.max_load_kg = max_load_kg
        self.require_special_license = require_special_license

    def vehicle_type(self):
        return 'van'
    
    def base_cleaning_time(self):
        return 50
    
    def wear_level(self):
        return 1
    
    def get_max_load_kg(self) -> int:
        return self.max_load_kg
    
    def get_require_special_license(self) -> bool:
        return self.require_special_license
    
    def info(self) -> None:
        dict_info: dict = super().info()
        dict_info['doors'] = self.get_max_load_kg()
        dict_info['is_cabrio'] = self.get_require_special_license()
        return dict_info

class FleetManager:

    def __init__(self, veichles:dict[str, Veichle]|None = None) -> None:
        self.veichles = veichles or {}

    def add(self, veichle: Veichle) -> bool:
        if veichle.get_id() in self.veichles:
            return False
        self.veichles[veichle.get_id()] = veichle
        return True
    
    def get(self, plate_id:str) -> Veichle:
        if plate_id not in self.veichles:
            return None
        return self.veichles[plate_id] 
    
    def update(self, plate_id:str, new_vehicle: Veichle) -> None:
        if plate_id not in self.veichles:
            return None
        self.veichles[plate_id] = new_vehicle

    def patch_status(self, plate_id: str, new_status: str) -> None:
        if plate_id not in self.veichles:
            return None
        self.veichles[plate_id].set_status(new_status)

    def delete(self, plate_id:str) -> bool:
        if plate_id not in self.veichles:
            return False
        self.veichles.pop(plate_id)
        Veichle._index_id.remove(plate_id)
        return True
    
    def list_all(self) -> list[dict]:
        return [veic.info() for veic in self.veichles.values()]
    
c1: Car = Car(id_targa='HA014AS', model='Panda', driver_name='Alice Bella', registration_year=2020, status='available',
                 doors=4, is_cabrio=False)
v1: Van = Van(id_targa='HA014A6', model='Panda', driver_name='Alice Bella', registration_year=2020, status='available',
                 max_load_kg=500, require_special_license=False)
print(c1.info())
print(v1.info())

fm1: FleetManager = FleetManager()
fm1.add(c1)
fm1.add(v1)

print(fm1.list_all())