'''
Exercise 9: Check Palindrome Number
Write a Python code to check if the given number is palindrome. 
A palindrome number is a number that is the same after reverse. 
For example, 545 is the palindrome number.
'''
# Versione 1   come stringa

number:str = input("\nScrivi il numero: ")

def polindrome_str(number):
    if number == number[::-1]:
        print(f"Il numero {number} è un polindrome\n")
    else:
        print(f"Il numero {number} non è un polindrome")

polindrome_str(number)
        
# Versione 2   come integer

number:int = int(input("\nScrivi un numero: "))

def polindrome_int(number:int):

    new_number:int = 0
    old_number:int = number

    while number > 0:
        resto:int = number % 10
        new_number = resto + new_number * 10 
        number:int = number // 10

    if old_number == new_number:
        print(f"Il numero {old_number} è un polindrome\n")
    else:
        print(f"Il numero {old_number} non è un polindrome")
    
    

polindrome_int(number)


