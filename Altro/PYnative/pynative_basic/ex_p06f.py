'''
Exercise 6: Display numbers divisible by 5
Write a Python code to display numbers from a list divisible by 5
'''

lista:list = [34, 50, 40, 45, 20, 14]

def devisible_5(lista):
    lista_div_5 = []
    for i in lista:
        if i % 5 == 0:
            lista_div_5.append(i)
        else:
            continue
    return lista_div_5

print(f"\nDalla lista {lista} \nSolo {devisible_5(lista)} sono divisibili per 5\n")