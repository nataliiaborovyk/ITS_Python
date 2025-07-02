'''
Exercise 3
Write a function print_numbers(), which takes a list of numbers as argument.
Using a for loop, print each number one by one.
'''
print("\n   Esercizio 3\n")

#function that takes a list of numbers as an argument

def print_numbers(lista:list):
    
    for i in lista:
        print(i)

print_numbers([1, 2, 3, 4])
