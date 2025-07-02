'''
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, write a Python code to return their product only 
if the product is equal to or lower than 1000. Otherwise, return their sum.
'''

def numbers(x:int, y:int):
    prod:int = x * y
    if prod <= 1000:
        print(f" il prodotto x * y = {prod}")
        return prod
    else:
        somma:int = x + y
        print(f" la somma x + y = {somma}")
        return somma
        
#numbers(30, 50)
numbers(89, 2)