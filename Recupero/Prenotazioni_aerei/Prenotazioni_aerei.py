from abc import ABC, abstractmethod

class Volo(ABC):
    _codice:str
    _max_posti:int

    def __init__(self, codice_volo:str, max_posti:int) -> None:
        self._codice_volo = codice_volo
        self._max_posti = max_posti
        self._prenotazioni = 0

    @abstractmethod
    def prenota_posto(self):
        pass

    @abstractmethod
    def posti_disponibili(self):
        pass

class VoloCommerciale(Volo):

    _posti_economica:int
    _posti_business:int
    _posti_prima:int
    _prenotazioni_economica:int
    _prenotazioni_business:int
    _prenotazioni_prima:int

    def __init__(self, codice_volo:str, max_posti:int) -> None:
        super().__init__(codice_volo, max_posti)
        # super().__init__(max_posti)
        self._posti_economica = int(0.7 * max_posti)
        self._posti_business = int(0.2 * max_posti)
        self._posti_prima = int(0.1 * max_posti)
        self._prenotazioni_economica = 0
        self._prenotazioni_business = 0
        self._prenotazioni_prima = 0
        self._posti_disp = {}

    def posti_disponibili(self) -> dict:

        disp_econ: int = self._posti_economica - self._prenotazioni_economica
        disp_bus:int = self._posti_business - self._prenotazioni_business
        disp_prima: int = self._posti_prima - self._prenotazioni_prima
        disp_totali: int = disp_econ + disp_bus + disp_prima

        self._posti_disp: dict = {"Posti disponibili": disp_totali, 
                                   "Classe economica": disp_econ,
                                   "Classe business": disp_bus,
                                   "Prima classe": disp_prima}
        return self._posti_disp
    
    def prenota_posto(self, posti: int, classe_servizio:str):
        self.posti_disponibili()
        if classe_servizio not in self._posti_disp:
            print(f"La classe {classe_servizio} non è presente nel volo {self._codice_volo}") 
        # for k, v in self._posti_disp.items():
        if posti <= self._posti_disp["Posti disponibili"]:
            if posti <= self._posti_disp[classe_servizio]:
                
                self._posti_disp[classe_servizio] -= posti
                self._prenotazioni += posti

                match classe_servizio:
                    case "Classe economica":
                        self._prenotazioni_economica += posti
                    case "Classe business":
                        self._prenotazioni_business += posti
                    case "Prima classe":
                        self._prenotazioni_prima += posti

                print(f"Hai prenotato {posti} in classe {classe_servizio} di volo{self._codice_volo}")
            else:
                print(f"Purtroppo non ci sono {posti} posti disponibili in {classe_servizio} di volo {self._codice_volo}")
        else:
            print(f"Il volo {self._codice_volo} è completo")

    def __str__(self) -> str:
        self.posti_disponibili()
        return f"Volo: {self._codice_volo} \nPosti totali: {self._max_posti} \
                \nClass Economica: max posti: {self._posti_economica}, prenotati: {self._prenotazioni_economica}, disponibili: {self._posti_disp['Classe economica']} \
                \nClass Business: max posti: {self._posti_business}, prenotati: {self._prenotazioni_business}, disponibili: {self._posti_disp['Classe business']} \
                \nClass Prima: max posti: {self._posti_prima}, prenotati: {self._prenotazioni_prima}, disponibili: {self._posti_disp['Prima classe']} "

class VoloCharter(Volo):
    _costo_volo: float
    _posti_prenotati: int
    _posti_disponibili: int

    def __init__(self, codice_volo:str, max_posti:int, costo_volo:float) -> None:
        super().__init__(codice_volo, max_posti)
        self._costo_volo = costo_volo
        self._posti_prenotati = 0
        self._posti_disponibili = self._max_posti
        self._prenotato = False

    def prenota_posto(self):
        if self._posti_disponibili == self._max_posti:
            self._posti_disponibili = 0
            self._posti_prenotati = self._max_posti
            self._prenotazioni = self._max_posti
            print(f"Il volo {self._codice_volo} è stato prenotato completamente")
        else:
            print(f"Purtroppo il volo {self._codice_volo} è gia prenotato")

    def posti_disponibili(self):
        return self._posti_disponibili
    
class CompagniaAerea:
    _nome: str
    _prezzo_standart: float
    _flotta: list[Volo]

    def __init__(self, nome:str, prezzo_standart:float) -> None:
        self._nome = nome
        self._prezzo_standart = prezzo_standart
        self._flotta = []

    def aggiungi_volo(self, volo:VoloCommerciale) -> None:
        if volo in self._flotta:
            raise ValueError("Errore, il volo è gia presente")
        self._flotta.append(volo)

    def rimuovi_volo(self, volo:VoloCommerciale) -> None:
        if volo not in self._flotta:
            raise ValueError("Errore, il volo non è presente")
        self._flotta.remove(volo)

    def mostra_flotta(self) -> str:
        return [i._codice_volo for i in self._flotta]
    
    def guadagno(self) -> float:
        guadagno: float = 0
        for i in self._flotta:
            if type(i) == VoloCommerciale:
                guadagno += ((i._prenotazioni_economica * self._prezzo_standart) 
                             + (i._prenotazioni_business * self._prezzo_standart * 2)
                             + (i._prenotazioni_prima * self._prezzo_standart * 3))
            elif type(i) == VoloCharter:
                guadagno += i._costo_volo
        return round(guadagno, 2)


if __name__ == "__main__":

    v1:VoloCommerciale = VoloCommerciale("AAA33", 150)
    print(v1)
    v1.prenota_posto(50, "Classe economica")
    print(v1)
    v1.prenota_posto(15, "Prima classe")
    print(v1)
    v1.prenota_posto(5, "Prima classe")
    print(v1)

    v2:VoloCharter = VoloCharter("BBB44", 100, 1000)
    print(v2.posti_disponibili())
    v2.prenota_posto()
    print(v2.posti_disponibili())
    v2.prenota_posto()

    ca: CompagniaAerea = CompagniaAerea("WizAir", 10)
    ca.aggiungi_volo(v1)
    ca.aggiungi_volo(v2)
    print(ca.guadagno())
    print(ca.mostra_flotta())