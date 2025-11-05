'''
Esercizio 2. 
 
Elaborare uno schema che consenta di stampare in output in maniera ricorsiva gli elementi di una lista in ordine inverso.

Una volta elaborato lo schema, appena consentitovi dal docente, scrivere una funzione ricorsiva in Python, chiamata printListBackward() che stampi in output gli elementi di una lista in ordine inverso, sfruttando la ricorsione.

Infine, scrivere un codice driver che, date le seguenti liste, stampi ogni lista in ordine inverso sfruttando la funzione ricorsiva implementata.

    lista1: 1, 2, 3, 4, 5
    lista2: "Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"
'''
#ritorna un elemento alla volta invertito
def printListBackward(lista:list[str]):
    if len(lista) == 1:
        print(lista[0])
    else:
        print(lista[-1])
        return printListBackward(lista[:-1])
    
l1 = [1,2,3,4,5]
printListBackward(l1)

#ritorna lista invertita
def printListBackward2(lista:list[str]):
    if len(lista) == 1:
        return lista
    else:
        return [lista[-1]] + printListBackward2(lista[:-1])
    
l1 = [1,2,3,4,5]
print(printListBackward2(l1))