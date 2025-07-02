'''
Exercise 1
Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, 
smaller, or equal to 5.
'''

print("\n   Esercizio 1\n")

#function that takes a number as an argument

def check_value(n):

    if n > 5:
        print(f"Numero {n} > 5")

    elif n < 5:
        print(f"Numero {n} < 5")
        
    else:
        print(f"Numero {n} = 5")

check_value(10)

check_value(3)

check_value(5)