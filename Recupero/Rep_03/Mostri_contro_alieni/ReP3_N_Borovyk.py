from random import randint, sample

class Creatura:

    _nome: str

    def __init__(self, nome:str) -> None:
        self.set_nome(nome)

    def set_nome(self, nome:str) -> None:
        if not isinstance(nome, str) or nome.strip() == "": #.strip() rimuove sli spazzi al inizio e alla fine
            self._nome = "Creatura Generica"
        else:
            self._nome = nome

    def get_nome(self) -> str:
        return self._nome
    
    def __str__(self) -> str:
        return f"Creatura: {self.get_nome()}"
    

class Alieno(Creatura):
    
    _matricola: int
    _munizioni: list[int]

    def __init__(self, nome:str) -> None:
        self._setMatricola()
        nome_corretto: str = f"Robot-{self.getMatricola()}"
        if nome != nome_corretto:
            print("Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola!")
            print("Reimpostazione nome Alieno in Corso!.....\n")
            nome_nuovo = nome_corretto
        super().__init__(nome_nuovo)
        self._setMunizioni()

    def _setMatricola(self) -> None:
        numero: int = randint(10000,90000)
        self._matricola = numero

    def _setMunizioni(self) -> None:
        munizioni: list[int] = [x**x for x in range(15)]
        self._munizioni = munizioni

    def getMatricola(self) -> int:
        return self._matricola
    
    def getMunizioni(self) -> list[int]:
        return self._munizioni
    
    def __str__(self) -> str:
        return f"Alieno: {self.get_nome()}"
    

class Mostro(Creatura):

    _urlo_vittoria: str
    _gemito_sconfitta: str
    _assalto: list[int]

    def __init__(self, nome:str, urlo_vittoria:str, gemito_sconfitta:str) -> None:
        super().__init__(nome)
        self._setVittoria(urlo_vittoria)
        self._setSconfitta(gemito_sconfitta)
        self._setAssalto()
    

    def _setAssalto(self) -> None:
        lista: list[int] = []
        while len(lista) < 15:
            num: int = randint(1,100)
            if num not in lista:
                lista.append(num)
        self._assalto = lista
        #  alternativa
        #self._assalto = sample(range(1, 101), 15)   #sample(... , n) prende n numeri casuali

    def getAssalto(self) -> list[int]:
        return self._assalto

    def _setVittoria(self, vittoria:str) -> None:
        if not isinstance(vittoria, str) or vittoria.strip() == "":  
            self._urlo_vittoria = "GRAAAHHH"
        else:
            self._urlo_vittoria = vittoria

    def get_urlo_vittoria(self) -> str:
        return self._urlo_vittoria

    def _setSconfitta(self, sconfitta:str) -> None:
        if not isinstance(sconfitta, str) or sconfitta.strip() == "":
            self._gemito_sconfitta = "Uuurghhh"
        else:
            self._gemito_sconfitta = sconfitta

    def get_gemito_sconfitta(self) -> str:
        return self._gemito_sconfitta

    def __str__(self) -> str:
        nome:str = self.get_nome()
        nome_nuovo:str = ""
        for i in range(len(nome)):
            if i % 2 == 0:
                nome_nuovo += nome[i].lower()
            else:
                nome_nuovo += nome[i].upper()
        return f"Mostro: {nome_nuovo}"


def pariUguali(a: list[int], b: list[int]) -> list[int]:
    c: list[int] = []
    if len(a) != len(b):
        raise ValueError("Le liste hanno lungezza diversa")
    for i in range(len(a)):
            if a[i] % 2 == 0 and b[i] % 2 == 0:
                c.append(1)
            else:
                c.append(0)
    return c
    #   alternativa
    #return [1 if a[i] % 2 == 0 and b[i] % 2 == 0 else 0 for i in range(len(a))]

def combattimento(a: Alieno, m: Mostro) -> Alieno | Mostro:
    if not isinstance(a, Alieno):
        raise ValueError("Errore, inserisci un Alieno")
        return None
    if not isinstance(m, Mostro):
        raise ValueError("Errore, inserisci un Mostro")
        return None
    result:list[int] = pariUguali(a.getMunizioni(), m.getAssalto())
    cont: int = 0
    for i in result:
        if i == 1:
            cont += 1
    if cont > 4:
        for i in range(3):
            print(m.get_urlo_vittoria())
        return m
    else:
        print(m.get_gemito_sconfitta())
        return a


def proclamaVincitore(c: Creatura):
    frase: str = c.__str__()
    lungezza: int = len(frase) + 10
    altezza: int = 5
    for i in range(altezza):
        if i == 0 or i == altezza - 1:
            print("*" * lungezza)
        elif i == 2:
            print("*" + (" " * 4) + frase + (" " * 4) + "*")
        else:
            print("*" + (" " * (lungezza-2)) + "*")
            

    
if __name__ == "__main__":

    print("\n-----------Versione 1----------\n")

    a1:Alieno = Alieno("Robot-41119")
    print(a1)
    munizioni:list[int] = a1.getMunizioni()
    print("Munizioni: ", munizioni)
    print()
    print()
    m1:Mostro = Mostro("gOrThOr", "ayayayayaya!!!!!", "noeeeeoo")
    print(m1)
    assalto:list[int] = m1.getAssalto()
    print("Assalto: ", assalto)
    print()
    print()
    print("Combattimento")
    print()
    vincitore = combattimento(a1, m1)
    print()
    if isinstance(vincitore, Alieno):
        print("Alieni anno vinto!!!")
    else:
        print("Mostri hanno vinto!!!")
    proclamaVincitore(vincitore) 

    print("\n-------------Versione 2------------\n")

    a2:Alieno = Alieno("Robot-41119")
    print(a2)
    munizioni:list[int] = a2.getMunizioni()
    print("Munizioni: ", munizioni)
    print()
    print()
    m2:Mostro = Mostro("    ", "    ", "     ")
    print(m2)
    assalto:list[int] = m2.getAssalto()
    print("Assalto: ", assalto)
    print()
    print()
    print("Combattimento")
    print()
    vincitore = combattimento(a2, m2)
    print()
    if isinstance(vincitore, Alieno):
        print("Alieni anno vinto!!!")
    else:
        print("Mostri hanno vinto!!!")
    proclamaVincitore(vincitore)
