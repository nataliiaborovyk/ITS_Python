'''
Exercise 3: Return multiple values from a function
Write a program to create function calculation() such that it can accept two variables 
and calculate addition and subtraction. Also, it must return both addition 
and subtraction in a single return call.
'''

def calculation(x:float, y:float):
    addition:float = x + y
    subtraction:float = x - y
    return addition, subtraction

num_1:float = float(input("\nInserisci x = "))
num_2:float = float(input("Inserisci y = "))

addition, subtraction = calculation(num_1, num_2) 
#print(f"x = {num_1} y = {num_2} ")
print(f"\nx + y = {addition}\nx - y = {subtraction}")