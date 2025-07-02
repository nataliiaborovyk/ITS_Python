'''
Exercise 4
Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, 
“smaller” if it’s smaller than 5, and “equal” if it’s equal to 5.
'''

print("\n   Esercizio 4\n")

#function that takes a list of numbers as an argument

def check_each(lista:list):

    for i in lista:

        if i > 5:
            print(f"\n{i} is bigger then 5")

        elif i < 5:
            print(f"\n{i} is smaller then 5")

        else:
            print(f"\n{i} is equal to 5")

check_each([3, 5, 7])