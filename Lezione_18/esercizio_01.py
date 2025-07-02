import math

'''
Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). 
Handle ValueError if the input is negative by returning an informative message.
'''

def safe_sqrt(number:int) -> None:
   
    try:
        square = math.sqrt(number)
        print(square)
    except ValueError as error:
        print(error)


safe_sqrt(2)

safe_sqrt(-2)


def safe_sqrt_2(number:int) -> float:
   
    try:
        square = math.sqrt(number)
        return square
    except ValueError as error:
        return error


print("\n",safe_sqrt_2(2))

print(safe_sqrt_2(-2))

type(safe_sqrt(22))