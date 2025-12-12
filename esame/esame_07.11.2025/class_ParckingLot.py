'''
Classe ParkingLot
Attributi
spaces: dict[int, dict]
 Dizionario che mappa il numero del posto (intero) ai dettagli del posto.
 I dettagli sono un dizionario con:
    "occupato": bool
    "targa": str oppure None

Metodi
add_space(numero: int) -> bool
 Controlla se il numero (il posto) esiste già in spaces.
 Se sì, restituisce False.
 Altrimenti, aggiunge il nuovo posto (impostandolo come occupato=False e targa=None) e restituisce True.

remove_space(numero: int) -> dict | str
 Cerca il numero in spaces.
 Se non esiste, restituisce "Errore: posto inesistente."
 Se esiste ma occupato=True, restituisce "Errore: posto occupato."
 Se esiste ed è libero (occupato=False), lo rimuove da spaces e restituisce un dizionario contenente solo i dettagli del posto rimosso.

park_car(numero: int, targa: str) -> str
 Cerca il numero in spaces.
 Se non esiste, restituisce "Errore: posto inesistente."
 Se esiste ma occupato=True, restituisce "Errore: posto già occupato."
 Se esiste ed è libero, imposta occupato=True, salva la targa e restituisce "Auto parcheggiata con successo."

leave_space(numero: int) -> str
 Cerca il numero in spaces.
 Se non esiste, restituisce "Errore: posto inesistente."
 Se esiste ma occupato=False, restituisce "Errore: posto già libero."
 Se esiste ed è occupato, imposta occupato=False, cancella la targa (targa=None) e restituisce "Posto liberato con successo."

list_free_spaces() -> list[int]
 Scorre tutti i posti in spaces e restituisce una lista contenente i numeri (le chiavi) di solo quei posti che hanno occupato=False.

get_space_info(numero: int) -> dict | str
 Cerca numero in spaces.
 Se non esiste, restituisce "Errore: posto inesistente."
 Altrimenti, restituisce il dizionario interno contenente i dettagli di quel posto (stato di occupazione e targa).
 (es. { "occupato": True, "targa": "AB123CD" })

'''

class ParkingLot:
    def __init__(self) -> None:
        self.spaces: dict[int, dict] = {}

    def add_space(self, numero: int) -> bool:
        if numero in self.spaces:
            return False
        self.spaces[numero] = {"occupato": False, "targa": None}
        return True

    def remove_space(self, numero: int) -> dict | str:
        if numero not in self.spaces:
            return "Errore, posto inesistente"
        if self.spaces[numero]["occupato"]:
            return "Errore, posto occupato"
        diz: dict = self.spaces.pop(numero)
        return diz

    def park_car(self, numero: int, targa: str) -> str:
        if numero not in self.spaces:
            return "Errore, posto inesistente"
        if self.spaces[numero]["occupato"]:
            return "Errore, posto già occupato"
        self.spaces[numero]["occupato"] = True
        self.spaces[numero]["targa"] = targa
        return "Auto parcheggiata con successo"

    def leave_space(self, numero: int) -> str:
        if numero not in self.spaces:
            return "Errore, posto inesistente"
        if not self.spaces[numero]["occupato"]:
            return "Errore, posto già libero"
        self.spaces[numero]["occupato"] = False
        self.spaces[numero]["targa"] = None
        return "Posto liberato con successo"

    def list_free_spaces(self) -> list[int]:
        free: list[int] = []
        for k, v in self.spaces.items():
            if not v["occupato"]:
                free.append(k)
        return free

    def get_space_info(self, numero: int) -> dict | str:
        if numero not in self.spaces:
            return "Errore, posto inesistente"
        return self.spaces[numero]

