'''
6-9. Favorite Places: Make a dictionary called favorite_places. 
Think of three names to use as keys in the dictionary, and store
 one to three favorite places for each person. To make this exercise 
 a bit more interesting, ask some friends to name a few of their 
 favorite places. Loop through the dictionary, and print each 
 person’s name and their favorite places.
'''

#esercizio_6-9
print(" \n   Esercizio_6-9\n")

favorite_place: dict[str, str] = {
    "Chiara": "Roma",
    "Daniele": "Valenzia",
    "Esubalew": "Cancune",
    "Gian Marco": "Bali"}
for k, v in favorite_place.items():
    print(f"Il posto preferito di {k} è {v}")