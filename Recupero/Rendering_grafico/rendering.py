from abc import ABC, abstractmethod

class Forma(ABC):

    __nome: str

    def __init__(self, nome: str) -> None:
        self.__nome = nome

    def get_nome(self) -> str:
        return self.__nome

    @abstractmethod
    def getArea(self) -> str:
        pass
    
    @abstractmethod
    def render(self) -> str:
        pass


class Quadrato(Forma):

    __lato: int

    def __init__(self, lato: int) -> None:
        self.__lato = lato
        super().__init__("Quadrato")

    def getArea(self) -> int:
        return f"L'area del quadrato = {self.__lato**2}"
    
    def render(self) -> str:
        for i in range(self.__lato):
            if i == 0 or i == self.__lato - 1:
                print("*" * self.__lato)
            else:
                print("*" + " " * (self.__lato - 2) + "*")

        
class Rettangolo(Forma):

    __h: int
    __l: int

    def __init__(self, h: float, l: int) -> None:
        self.__h = h
        self.__l = l
        super().__init__("Rettangolo")

    def  getArea(self) -> int:
        return f"L'area del rettangolo = {self.__h * self.__l}"

    def render(self) -> str:
        for i in range(self.__h):
            if i == 0 or i == self.__h - 1:
                print("*" * self.__l)
            else:
                print("*" + " " * (self.__l - 2) + "*")

    
class Triangolo(Forma):

    __lato: int

    def __init__(self, lato: int) -> None:
        self.__lato = lato
        super().__init__("Triangolo")

    def getArea(self) -> float:
        return f"L'area del tiangolo = {(self.__lato ** 2) / 2}"
    
    def render(self) -> str:
        print(f"Triangolo: base = {self.__lato} e altezza = {self.__lato}")
        for i in range(1, self.__lato + 1):
            if i < 3 or i == self.__lato:
                print(f"*"*i)
            else:
                print("*" + " "*(i-2) + "*")


if __name__ == "__main__":

    t1: Triangolo = Triangolo(7)
    print(t1.getArea())
    t1.render()

    q1:Quadrato = Quadrato(5)
    print(q1.getArea())
    q1.render()

    r1:Rettangolo = Rettangolo(5,9)
    print(r1.getArea())
    r1.render()

