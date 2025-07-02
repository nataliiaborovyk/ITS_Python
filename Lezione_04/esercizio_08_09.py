'''
8-9. Messages: Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message.
'''
print("\n   Esercizio 8-9")

# VERSIONE 1
print("\n Versione 1")

lista: list = ["ciao", "hello", "privet", "nihao"]

def saluti(*args):
    print(*args)

saluti(*lista)

# VERSIONE 2
print("\n Versione 2")

def show_messages(*args) -> str:
    for i in args:
        print(i)

lista: list = ["ciao", "hello", "privet", "nihao"]
show_messages(*lista)

