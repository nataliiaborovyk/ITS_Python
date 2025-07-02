'''
8-7. Album: Write a function called make_album() that builds 
a dictionary describing a music album. The function should take 
in an artist name and an album title, and it should return 
a dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing different albums. 
Print each return value to show that the  dictionaries are storing 
the album information correctly. 
Use None to add an optional 
parameter to make_album() that allows you to store the number 
of songs on an album. If the calling line includes a value for the number 
 songs, add that value to the album’s dictionary. Make at least one 
 new function call that includes the number of songs on an album.
'''

print("\n   Esercizio 8-7\n")

#function that builds a dictionary describing a music album
def make_album(name:str, title:str, songs:int = None) -> dict[str, str, str]: 
        return {"Artist": name, "Album": title, "songs": songs}

diz_1: dict[str, str] = make_album("Lauro", "Amore", 5)
for k,v in diz_1.items():
    print(f" {k}: {v}")

print("")  #per distanziare un dizionario dal altro nel output
diz_2: dict[str, str] = make_album("Queen", "We will rock you")
for k,v in diz_2.items():
    print(f" {k}: {v}")

print("")
diz_3: dict[str, str] = make_album("Beatles", "Yesterday", 10)
for k,v in diz_3.items():
    print(f" {k}: {v}")



