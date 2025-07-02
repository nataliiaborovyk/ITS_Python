'''
8-11. Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.
'''

print("\n   Esercizio 8-11")


def show_messages(*args):
    for i in args:
        print(i)

lista_saluti: list = ["ciao", "hello", "privet", "nihao"]
show_messages("La lista dei messaggi: ", *lista_saluti)


def send_messages(lista1: list[str], lista2:list[str]):
    for i in lista1:
        lista2.append(i)
    lista1.clear()
    print("\nLa lista dei messaggi: ", *lista1)
    print("\nLa lista dei messaggi inviati: ", *lista2)

mesaggi_inviati:list = []

send_messages(lista_saluti[:], mesaggi_inviati) #do alla funzione la copia dlla lista ma originale rimane

print(f"\nLa lista dei messaggi originale: ", *lista_saluti)