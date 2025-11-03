'''
### B3.I.2 — Abstract Payment (classi astratte + override)
Task.
 Progettare un sistema di pagamenti con una classe astratta Payment.
 Ogni sottoclasse deve implementare il metodo authorize(amount: float) con regole specifiche.

Classe astratta Payment (ABC)
Attributi:
Nessuno obbligatorio.


Metodi astratti:
authorize(amount: float) -> bool:
 verifica se il pagamento può essere autorizzato in base al tipo di pagamento e all’importo.



Classe CardPayment(Payment)
Attributi:
card_number: str


Metodi:
authorize(amount: float) -> bool:
 restituisce True solo se il numero della carta ha 16 cifre e amount > 0;
 altrimenti restituisce False.



Classe CashPayment(Payment)
Attributi:
currency: str


Metodi:
authorize(amount: float) -> bool:
 restituisce True solo se la valuta è "EUR" o "USD" e l’importo è multiplo di 0.5;
 altrimenti restituisce False.



Driver:
if __name__ == "__main__":
    p1 = CardPayment("1234567890123456")
    p2 = CashPayment("EUR")
    p3 = CashPayment("JPY")

    print(p1.authorize(20))   # True
    print(p2.authorize(10.5)) # True
    print(p3.authorize(10))   # False

'''

from abc import ABC, abstractmethod
import re

class Payment(ABC):

    @abstractmethod
    def authorize(self, amount: float) -> bool:
        pass


class CardPayment(Payment):

    def __init__(self, card_number:str) -> None:
        self.card_number:str = card_number

    def authorize(self, amount:float) -> bool:
        if isinstance(self.card_number, str) \
           and len(self.card_number) == 16 \
           and self.card_number.isdigit() \
           and amount > 0:
            return True
        else:
            return False
        
class CashPayment(Payment):

    def __init__(self, currency:str):
        self.currency = currency

    def authorize(self, amount:float):
        if amount % 0.5 == 0 and self.currency in ("EUR", "USD"):
            return True
        else:
            return False

        
if __name__ == "__main__":
    p1 = CardPayment("1234567890123459")
    p2 = CashPayment("EUR")
    p3 = CashPayment("JPY")

    print(p1.authorize(20))   # True
    print(p2.authorize(10.5)) # True
    print(p3.authorize(10))   # False