from abc import ABC, abstractmethod
import re

class Payment(ABC):

    @abstractmethod
    def autorize(self, amount: float) -> bool:
        pass


class CardPayment(Payment):

    def __init__(self, card_number:str) -> None:
        self.card_number:str = card_number

    def autorize(self, amount:float) -> bool:
        
        