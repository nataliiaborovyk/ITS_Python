'''
Write a function called sum that takes a positive integer number n as input and returns the sum of the numbers from 0 to n.
If the input number n is negative, display an error message and the function must return None.
To implement the sum function, you must exclusively use a while loop and the parameter n passed as input to the function.
It is allowed to declare only one variable inside the function to manage the sum.
Then, call the function sum for n = -5 and n = 5.
'''
def recursiveSum(n:int) -> int:
    
    if n < 0:
        print("Error")
        return 0
    elif n == 0:
        return 0
    else:
        return int(n + recursiveSum(n-1))

print(recursiveSum(0))
print(recursiveSum(5))
print("")
print(recursiveSum(-5))
    
    