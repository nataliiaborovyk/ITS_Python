'''
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message 
and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.
'''

print("\n   Esercizio 8-10")


def show_messages(*args):
    for i in args:
        print(i)

lista_saluti: list = ["ciao", "hello", "privet", "nihao"]
show_messages("La lista dei mesaggi: ", *lista_saluti)


def send_messages(lista1: list[str], lista2:list[str]):
    for i in lista1:
        lista2.append(i)
    lista1.clear()
    print("\nLa lista dei mesaggi: ", *lista1)
    print("\nLa lista dei mesaggi inviati: ", *lista2)


mesaggi_inviati:list = []
send_messages(lista_saluti, mesaggi_inviati)
    
   