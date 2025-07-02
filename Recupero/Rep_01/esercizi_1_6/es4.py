'''
1) Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
oppure "Azione negata" a seconda delle condizioni che sono soddisfatte
'''


def function1(x,y,z) -> str:
    if x and (y or z):
        return "Azione permessa"
    else:
        return "Azione negata"
    
x1 = 5 < 3
y1 = 2 == 3
z1 = 7 > 1
print(function1(x1,y1,z1))

x2 = 3 < 5
y2 = 3 < 4
z2 = 3 < 2
print(function1(x2,y2,z2))