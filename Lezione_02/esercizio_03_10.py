'''
3-10. Every Function: Think of things you could store in a list. 
For example, you could make a list of mountains, rivers, countries, cities, 
languages, or anything else you’d like. Write a program that creates a list containing 
these items and then uses each function introduced in this chapter at least once.
'''

#esercizio_3-10
print("\n esercizio_3-10\n")

mylist: list = ["asterisco", "apice", "doppio aoice", "backslash", "hashtag"]
print(f"Lista: {mylist}")

mylist.sort()
print("\nLista in ordine alfabetico")
print(*mylist, sep= ", ")

mylist.sort(reverse=True)
print("\nLista in ordine alfabetico al contrario")
print(*mylist, sep= ", ")