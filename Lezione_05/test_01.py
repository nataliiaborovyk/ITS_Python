'''
Hai una lista di numeri interi. Il tuo compito è riorganizzare questa lista in modo che:
    tutti i numeri pari vengano prima di tutti i numeri dispari;
    l’ordine relativo tra pari e dispari va mantenuto;
    l’obiettivo è solo separare i pari dai dispari, con i pari che vengono per primi.

    print(even_odd_pattern([3, 6, 1, 8, 4, 7]))    [6, 8, 4, 3, 1, 7]
'''

def even_odd_pattern(numbers:list[int]) -> list[int]:
    lista_pari:list = []
    lista_dispari: list = []

    for i in numbers:
        if i % 2 == 0:
            lista_pari.append(i)
        else:
            lista_dispari.append(i)
    
    return lista_pari + lista_dispari


print(even_odd_pattern([3, 6, 1, 8, 4, 7]))