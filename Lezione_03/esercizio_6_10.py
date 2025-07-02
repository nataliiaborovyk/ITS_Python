'''
6-10. Favorite Numbers: Modify your program from Exercise 6-2 
so each person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers.
'''

#esercizio_6-10
print(" \n   Esercizio_6-10")

anna_num: list[int] = [7,5,77,56]
marco_num: list[int] = [17,94,8,3]
giuseppe_num: list[int] = [88,63,83,3]
federica_num: list[int] = [28,7,29,25]

mydict1: dict[str, list] = {
    "Anna": anna_num, 
    "Marco": marco_num,
    "Giuseppe": giuseppe_num,
    "Federica": federica_num}

for k, v in mydict1.items():
    print(f"A {k} piaciono i numeri: {v}")
    