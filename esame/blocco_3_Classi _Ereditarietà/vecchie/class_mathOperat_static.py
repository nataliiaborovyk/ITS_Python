'''
            
            Exercise 2: Implementing Static Methods

Create a class called MathOperations to group together some basic arithmetic functionality. Inside this class, define two static methods:
    add, which accepts two numeric parameters and returns their sum.
    multiply, which also takes two numeric parameters and returns their product.
Finally, write a small driver program to test the functionality of the add and multiply methods. This should involve calling both methods with sample inputs and printing the results to verify that they work correctly.
'''

class MathOperations:

    @staticmethod
    def add(a, b):
        return a+b
    
    @staticmethod
    def multiply(a, b):
        return a*b
    
if __name__ == "__main__":

    somma = MathOperations.add(2,4)
    prod = MathOperations.multiply(3,4)

    print("Somma:", somma)
    print("Prodotto:", prod)