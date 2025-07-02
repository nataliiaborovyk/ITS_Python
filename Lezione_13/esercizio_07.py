'''
Una produttoria è definita come il prodotto di un certo numero n di fattori, con n intero positivo. 
Sia Pi3 una produttoria definita come segue:
Pi3 = (1**3) * (2**3) * (3**3) * ... * (n**3)  
'''


def produttoria(n:int) -> int:
    if n == 1:
        return 1
    else:
        return n**3 * produttoria(n-1)
    
print("\n", produttoria(5), "\n")