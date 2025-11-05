'''
Funzioni, For, While, If, Elif ed Else
1) Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è 
soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
oppure "Azione negata" a seconda delle condizioni che sono soddisfatte.

2) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.

3) Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 45
'''

#1
def verifica(x,y,z):
    if x==True and (y == True or z == True):
        print("Azione permessa")
    else:
        print('Azione negata')
    
verifica(5<7,4==4, 7>8)


#2
def molt(lista:list[int],x:int) -> int:
    prod = 1
    for i in lista:
        if i < x:
            prod *= i
    return prod

print(molt([1,2,3,4,5],5))

#3
def cicli():
    for i in range(2,15,2):
        print(i, end=" ")
    print()

    for i in range(1,14,3):
        print(i, end=" ")
    print()

    for i in range(30,-1,-5):
        print(i, end=" ")
    print()

    for i in range(5,46,10):
        print(i, end=" ")
    print()

cicli()