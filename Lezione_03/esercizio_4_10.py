'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
'''

print("\n Esercizio 4-10 \n")

animals: list = ["Dog", "Cat", "Parrot"]
pizza: list = ["Margherita", "Marinara", "Napoletana"]
lista: list = animals + pizza
print("Lista: ", *lista, sep=", ")

print("\nI primi 3 elementi sono: ", *lista[0:3], sep=", ")
for i in lista[:3]:
    print(i)

meta:int = len(lista)//2 
lista_metà:list = lista[meta-1:meta+2]

print("\nGli elementi in mezzo sono: ", *lista_metà)

print("\nGli ultimi 3 elementi sono: ", *lista[-3:])