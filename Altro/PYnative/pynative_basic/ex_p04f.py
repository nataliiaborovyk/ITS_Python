'''
Exercise 4: Remove first n characters from a string
Write a Python code to remove characters from a string from 0 to n and return a new string.
For Example:
    remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
    remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.
'''

frase_1: str = input("\nScrivi una frase: ")
val_1:int = int(input("Scrivi quanti carratteri vuoi eliminare: "))

frase_2: str = input("\nScrivi un altra frase: ")
val_2:int = int(input("Scrivi quanti carratteri vuoi eliminare: "))

def remove_chars(frase:str, val):
    if val <= len(frase):
        frase_new: str = frase[val:]
        print(frase_new)
    else:
        print("Errore")
    

remove_chars(frase_1, val_1)

remove_chars(frase_2, val_2)