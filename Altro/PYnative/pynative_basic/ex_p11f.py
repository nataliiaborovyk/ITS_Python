'''
Exercise 11: Get each digit from a number in the reverse order.
For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
'''
# Versione 1   come stringa

number:str = input("\nScrivi un numero: ")

for i in range(1, len(number)+1):
    print(number[-i], end= " ")
print("")

# Versione 2   come integer

number:int = int(input("\nScrivi un numero: "))

def reverse(number:int):
    while number > 0:
        resto:int = number % 10
        number:int = number // 10
        print(resto, end=" ")
    print("")

reverse(number)