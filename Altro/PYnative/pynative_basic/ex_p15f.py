'''
Exercise 15: Get an int value of base raises to the power of exponent
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
Note here exp is a non-negative integer, and the base is an integer.
'''

base:int = int(input("\nValue of base: "))
exp:int = int(input("Value of exponent: "))

def exponent(base:int, exp:int):
    if base % 1 == 0 and exp >= 0:
        result = 1
        for i in range(exp):
            result *= base
        return result
    else: 
        print("\nError")
    

print(f"\n{base} ** {exp} = {exponent(base,exp)}\n")
