
from random import randint

def generaMatrice(dim:int) -> list[list[int]]:
    matrice: list[list[int]] = []
    for i in range(dim):
        lista: list[int] = []
        # for k in range(dim):
        #     x: int = randint(0, 13)
        #     if x != lista[0]:
        #         lista.append(x)
        
        while len(lista) < dim:
            x: int = randint(0, 13)
            if len(lista) == 0:
                lista.append(x)
            else:
                if x != lista[0]:
                    lista.append(x)
        matrice.append(lista)
    return matrice



def printMAT(matrice) -> str:
    for i in range(len(matrice)):
        for k in range(len(matrice[i])):
            print(f"{matrice[i][k]:<5}", end="")
        print("\n")

# printMAT(matrice)


def calcolaCarico(matrice:list[list[int]], r:int, c:int) -> int:
    somma_riga: int = sum(matrice[r])
    somma_colonna: int = 0
    for i in range(len(matrice)):
        for k in range(len(matrice[i])):
            if k == c:
                somma_colonna += matrice[i][k]
    carico_posizione: int = somma_riga - somma_colonna
    return carico_posizione

# print(f"Carico della matrice: ", calcolaCarico(matrice, 1, 1), "con indici (1, 1)")

    
def caricoNullo(matrice) -> list[tuple[int]]:
    lista: list[tuple[int]] = []
    for i in range(len(matrice)):
        for k in range(len(matrice[i])):
            calcolo: int = calcolaCarico(matrice, i, k)
            if calcolo == 0:
                lista.append((i, k)) 
    return f"Carico è nullo per indici {lista}"

# print(f"Carico è nullo per indici", caricoNullo(matrice))

def caricoMax(matrice) -> tuple:
    diz: dict[int,tuple] = {}
    for i in range(len(matrice)):
        for k in range(len(matrice[i])):
            x:int = calcolaCarico(matrice, i, k)
            diz[x] = (i,k)
    valore_max: int = max(diz.keys())
    for k, v in diz.items():
        if k == valore_max:
            #print(f"Carico massimo: {valore_max} per indici: ")
            return k, v
        
#print(caricoMax(matrice))

def caricoMin(matrice) -> tuple:
    diz: dict[int,tuple] = {}
    for i in range(len(matrice)):
        for k in range(len(matrice[i])):
            x:int = calcolaCarico(matrice, i, k)
            diz[x] = (i,k)
    valore_min: int = min(diz.keys())
    for k, v in diz.items():
        if k == valore_min:
            #print(f"Carico minimo: {valore_min} per indici: ")
            return k, v
        
#print(caricoMin(matrice))

if __name__ == "__main__":
    matrice: list[list[int]] = generaMatrice(5)
    printMAT(matrice)
    print(f"Carico della matrice: ", calcolaCarico(matrice, 1, 1), "con indici (1, 1)")
    print(caricoNullo(matrice))
    tupla1:tuple = caricoMax(matrice)
    print(f"Carico massimo: {tupla1[0]} per indici: {tupla1[1]}")
    tupla2:tuple = caricoMin(matrice)
    print(f"Carico minimo: {tupla2[0]} per indici: {tupla2[1]}")
    
    print("\nVerifico se carico max è giusto")
    print(f"Carico della matrice:", calcolaCarico(matrice, tupla1[1][0], tupla1[1][1]), f"per indici {tupla1[1]}")

    print("\nVerifico se carico min è giusto")
    print(f"Carico della matrice:", calcolaCarico(matrice, tupla2[1][0], tupla2[1][1]), f"per indici {tupla2[1]}")