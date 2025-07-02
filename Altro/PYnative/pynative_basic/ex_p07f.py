'''
Exercise 7: Find the number of occurrences of a substring in a string
Write a Python code to find how often the substring “Emma” appears in the given string.
'''
# Versione 1

string:str = input("\nScrivi il testo: ")

substring:str = input("\nScrivi cosa cerchi nel testo: ")

def ricerca(string:str, substring:str):
    return string.count(substring)

print(f"Ci sono {ricerca(string, substring)} perole \"{substring}\" nel testo")


# Versione 2

string:str = input("\nScrivi il testo: ")

substring:str = input("\nScrivi cosa cerchi nel testo: ")

def ricerca(string:str, substring:str):
    x:int = len(substring)
    cont:int = 0
    for i in range(len(string)):
        if string[i:x+i] == substring:
            cont += 1
        else:
            continue
    return cont

print(f"Ci sono {ricerca(string, substring)} perole \"{substring}\" nel testo")
