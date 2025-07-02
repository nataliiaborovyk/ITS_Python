from typing import Any

class Frazione:

    _numeratore: Any
    _denominatore: Any

    def __init__(self, numeratore: Any, denominatore: Any) -> None:
        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)

    def set_numeratore(self, numeratore: Any) -> None:
        if type(numeratore) == int:
            self._numeratore = numeratore
        else: 
            self._numeratore = 13

    def set_denominatore(self, denominatore:Any) -> None:
        if type(denominatore) == int and denominatore != 0:
            self._denominatore = denominatore
        elif type(denominatore) == int and denominatore == 0:
            self._denominatore = 5

    def get_numeratore(self) -> int:
        return self._numeratore 
    
    def get_denominatore(self) -> int:
        return self._denominatore
    
    def value(self) -> float:
        return round(self._numeratore/self._denominatore, 3)
    
    def __str__(self) -> str:
        return f"{self.get_numeratore()} / {self.get_denominatore()}"
    
    def __repr__(self) -> str:
        return str(self)
    

def mcd(x: int, y: int):
    if y > x:
        x, y = y, x
    
    divisori_x: list[int] = []
    for i in range(1,x+1):
        if x % i == 0:
            divisori_x.append(i)

    divisori_y: list[int] = []
    for i in range(1,y+1):
        if y % i == 0:
            divisori_y.append(i)
    
    divisori_comuni:list[int] = []
    for i in divisori_x:
        if i in divisori_y:
            divisori_comuni.append(i)

    mcd:int = max(divisori_comuni)
    return mcd

def mcd2(x:int, y:int):
    end:int = x
    if x > y:
        end = x
    max_divisor: int = 1
    for i in range(1, end + 1):
        if x % i == 0 and y % i == 0:
            if i > max_divisor:
                max_divisor = i
    return max_divisor

def semplifica(lista:list[Frazione]) -> list[Frazione]:
    frazioni_irriducibili: list[Frazione] = []
    for i in lista:
        mcd_i: int = mcd(i.get_numeratore(), i.get_denominatore())
        if mcd_i == 1:
            frazioni_irriducibili.append(i)
        elif mcd_i != 1:
            numeratore_sempl: int = int(i.get_numeratore() / mcd_i)
            denominatore_sempl: int = int(i.get_denominatore() / mcd_i)
            frazioni_irriducibili.append(Frazione(numeratore_sempl, denominatore_sempl))
    return frazioni_irriducibili


def fractionCompare(lista_o, lista_s) -> str:
    if len(lista_o) == len(lista_s):
        for i in range(len(lista_o)):
            print(f"Frazione originale: {lista_o[i]}, Valore frazione originale: {lista_o[i].value()} ... Frazione ridotta: {lista_s[i]}, Valore frazione ridotta: {lista_s[i].value()}")
            if lista_o[i].value() != lista_s[i].value():
                print(f"Frazione originale: {lista_o[i]}, Valore frazione originale: {lista_o[i].value()} ... NON È UGUALE A ... Frazione ridotta: {lista_s[i]}, Valore frazione ridotta: {lista_s[i].value()}")



if __name__ == "__main__":
    n1 = Frazione(7, 9)
    print(n1)

    n2 = Frazione(7.8, 9)
    print(n2)
            
    print(n1.value())

    print(mcd(8,12))

    lista = [Frazione(2,6), Frazione(4,12), Frazione(1,5)]
    print(semplifica(lista))

    lista_originale:list[Frazione] = [Frazione(2,6), Frazione(4,12), Frazione(1,5)]
    lista_semplificata: list[Frazione] = semplifica(lista_originale)

    fractionCompare(lista_originale, lista_semplificata)

    l:list[Frazione]=[]
    
    l.append(Frazione(2.5,0))
    l.append(Frazione(1,2))
    l.append(Frazione(2,4))
    l.append(Frazione(3,5))
    l.append(Frazione(6,9))
    l.append(Frazione(4,7))
    l.append(Frazione(24,36))
    l.append(Frazione(12,36))
    l.append(Frazione(40,60))
    l.append(Frazione(5,11))
    l.append(Frazione(10,45))
    l.append(Frazione(42,78))
    l.append(Frazione(9,15))

    l_s=semplifica(l)

    fractionCompare(l,l_s)