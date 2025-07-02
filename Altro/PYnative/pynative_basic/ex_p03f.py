'''
Exercise 3: Print characters present at an even index number
Write a Python code to accept a string from the user and display characters present at an even index number.
For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
'''
#versione 1 (stampare solo pari)

frase: str = input("\nScrivi una frase: ")

for i in range(0, len(frase)+1, 2):
    print(frase[i], end=" ")


#versione 2 (stampare senza vocali)

frase: str = input("\nScrivi una frase: ")

for i in frase:
    match i:
        case "a":
            continue
        case "e":
            continue
        case "i":
            continue
        case "u":
            continue
        case "o":
            continue
        case _:
            print(i, end=" ")

print("")