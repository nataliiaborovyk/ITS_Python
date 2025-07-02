'''
Exercise 5
Write a function add_one(). It takes an integer as argument. 
The function adds 1 to the integer and returns it.
Write another function add_one_to_list(). It takes a list of integers as argument.
Define a variable new_list in this function.
Using a for loop, iterate through the argument list.
Using add_one(), fill new_list with integers from the argument list incremented
by 1.
Print new_list.
'''

print("\n   Esercizio 5\n")

#function adds 1 to the integer and returns it
def add_one(x: int):
    return x + 1

print(add_one(1))

#function incremented list by 1
def add_one_to_list(lista:int):
    new_list:list = []
    for i in lista:
        new_list.append(add_one(i))
    return new_list

print(add_one_to_list([1, 2, 3, 4]))



