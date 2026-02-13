from typing import TYPE_CHECKING, Any, Self
from abc import ABC, abstractmethod
from custom_types import Status
from Index import Index

class Device(ABC):

    
    _index_id: Index[int, Self] = Index('Device') 

    def __init__(self, *, model:str, customer_name:str, purchase_year:int, 
               status: str = 'received') -> None:
        self._set_id()
        self.model = model
        self.customer_name = customer_name
        self.purchase_year = purchase_year
        self.status = status

    
    @classmethod
    def device_con_id(cls, id: Any) -> Self|None:
        return cls._index_id.get(id)
    
    @classmethod
    def tutti_devices(cls):
        return cls._index_id.all()

    # @classmethod
    # def _delete_id(cls, id:str) -> None:
    #     if id not in Device._id_usate:
    #         raise ValueError('Id non esiste')
    #     Device._id_usate.remove(id)


    def _set_id(self) -> None:
        key_list = list(self._index_id.all_keys())
        if len(key_list) > 0:
            last_id = max(key_list)
            id = last_id + 1
        else:
            id = 0
        self._index_id.add(id, self)
        self.id = id

    @abstractmethod
    def devise_type(self):
        pass

    @abstractmethod
    def base_diagnosis_time(self):
        pass

    @abstractmethod
    def repair_complexity(self):
        pass

    def info(self) -> dict[str, int|str|Status|bool]:
        return {
            "id": self.get_id(),
            "device_type": self.devise_type(),
            "model": self.model,
            "customer_name": self.customer_name,
            "purchase_year": self.purchase_year,
            "status": self.status,          
        }
    
    def estimated_total_time(self, factor: float = 1.0) -> int:
        result: int = int(self.base_diagnosis_time() * factor + self.repair_complexity() * 30)
        return result

    def get_id(self) -> int:
        return self.id
    
    def get_status(self) -> str:
        return self.status
    
    def _update_status(self, new_status: str) -> None:
        self.status = new_status
    
    

class Smartphone(Device):

    def __init__(self, *, model:str, customer_name:str, purchase_year:int,  
                 has_protective_case: bool, storage_gb: int, status: str = 'received') -> None:
        super().__init__(model=model, customer_name=customer_name, purchase_year=purchase_year, status=status)
        self.has_protective_case = has_protective_case
        self.storage_gb = storage_gb

    def devise_type(self):
        return 'smartphone'
    
    def base_diagnosis_time(self) -> int:
        return 20
    
    def repair_complexity(self) -> int:
        return 2
    
    def info(self) -> dict:
        info_gen: dict[str, int|str|bool] = super().info()
        info_gen['has_protective_case'] = self.has_protective_case
        info_gen['storage_gb'] = self.storage_gb
        return info_gen
        
 
class Laptop(Device):

    def __init__(self, *, model:str, customer_name:str, purchase_year:int,  
                 has_dedicated_gpu: bool, screen_size_inches: float, status: str = 'received') -> None:
        super().__init__(model=model, customer_name=customer_name, purchase_year=purchase_year, status=status)
        self.has_dedicated_gpu = has_dedicated_gpu
        self.screen_size_inches = screen_size_inches

    def devise_type(self):
        return 'laptop'
    
    def base_diagnosis_time(self) -> int:
        return 40
    
    def repair_complexity(self) -> int:
        return 3
    
    def info(self) -> dict:
        info_gen: dict[str, int|str|bool] = super().info()
        info_gen['has_dedicated_gpu'] = self.has_dedicated_gpu
        info_gen['screen_size_inches'] = self.screen_size_inches
        return info_gen


class ServiceCenter:

    def __init__(self, devices: dict[str, Device]|None = None) -> None:
        self.devices = devices or {}

    def add(self, device:Smartphone|Laptop) -> bool:
        if device.get_id() in self.devices:
            return False
        self.devices[device.get_id()] = device
        return True
    
    def get(self, device_id:int) -> Device|None:
        if device_id not in self.devices:
            return None
        return self.devices[device_id]
    
    def update(self, device_id:int, new_device:Smartphone|Laptop) -> None:
        if device_id not in self.devices:
            raise ValueError('Dispositivo non esiste')
        self.devices[device_id] = new_device

    def patch_status(self, device_id:int, new_status:str ) -> None:
        if device_id not in self.devices:
            raise ValueError('Dispositivo non esiste')
        self.devices[device_id]._update_status(new_status)

    def delete(self, device_id:int) -> bool:
        if device_id not in self.devices:
            return False
        self.devices.pop(device_id)
        Device._index_id.remove(device_id)
        return True

    def list_all(self) -> list[Smartphone|Laptop]:
        return [dev.info() for dev in self.devices.values()]
    



sc1 = ServiceCenter()
tel1 = Smartphone(model="Samsung fe 30", customer_name="Alice Bella", 
                    purchase_year=2024, has_protective_case=True,  storage_gb=128)
pc1 = Laptop(model="Apple", customer_name="Alice Bella", 
                    purchase_year=2021, has_dedicated_gpu=True,  screen_size_inches=15.6)
sc1.add(tel1)
sc1.add(pc1)
print(tel1.get_id())
print(pc1.get_id())

print(sc1.list_all())
print(f"\nTempo per riparare tel: {tel1.estimated_total_time()} minuti")
print(f"\nTempo per riparare laptop: {pc1.estimated_total_time()} minuti")

sc1.patch_status(tel1.get_id(), 'repairing')
print(f"Nuovo stato tel: {tel1.get_status()}")

sc1.patch_status(pc1.get_id(), 'ready')
print(f"Nuovo stato tel: {pc1.get_status()}")



   


        