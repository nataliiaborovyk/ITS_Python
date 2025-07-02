'''
Exercise 5: Check if the first and last numbers of a list are the same
Write a code to return True if the list’s first and last numbers are the same. 
If the numbers are different, return False.
'''


def check_list(lista:list):
    if lista[0] == lista[-1]:
        return True
    else:
        return False
    
lista_1:list = [10, 20, 3, 50]
lista_2:list = [5, 2, 45, 5]

print(check_list(lista_1))
print(check_list(lista_2))

