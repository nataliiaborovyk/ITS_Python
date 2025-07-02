'''
Exercise 10: Merge two lists using the following condition
Given two lists of numbers, write a Python code to create a new list such that the latest list 
should contain odd numbers from the first list and even numbers from the second list.
'''

lista_1:list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_2:list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
new_list:list = []

def mix_list(lista_1, lista_2):
    for i in lista_1:
        if i % 2 != 0:
            new_list.append(i)
    for i in lista_2:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

print("\nLista 1: ", *lista_1, "\nLista 2: ", *lista_2, "\n")
print("Il risultato: ", *mix_list(lista_1, lista_2), "\n")