'''
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.
'''

#esercizio_3-8
print("\n esercizio_3-8\n")

loc_list: list = ["Japone", "America", "Swizzera", "Francia", "Nepal"]
print(*loc_list, sep= ", ")

sort_list = sorted(loc_list)
print("\nLista in ordine alfabetico")
print(*sort_list, sep= ", ")

sort_list.reverse()
print("\nLista in ordine alfabetico al contrario")
print(*sort_list, sep= ", ")

sort_list.reverse() 
print("\nLista di nuovo in ordine alfabetico")
print(*sort_list, sep= ", ")

loc_list.sort()
print("\nLista in ordine alfabetico")
print(*loc_list, sep= ", ")

loc_list.sort(reverse=True)
print("\nLista in ordine alfabetico al contrario")
print(*loc_list, sep= ", ")
