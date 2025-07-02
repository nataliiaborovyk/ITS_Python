'''
Write a Python function called countdown that takes a positive integer n as input 
and prints a countdown from n to zero.
If the input number is negative, display an error message.
To implement the function, you must exclusively use a while loop 
and the parameter n passed as input to the function.
Declaring any additional variables inside the function is not allowed.
Then, call the function with n = -5 and n = 5
'''
def countdown(num:int) -> None:

    if num >= 0:
        while True:
            print(num)
            num -= 1
            if num < 0:
                break
    
    else:
        print("Error! Inserted number is negative")

num:int = int(input("Inserisci il numero: "))

countdown(num)