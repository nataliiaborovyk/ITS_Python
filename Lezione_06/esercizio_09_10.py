'''
 Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. 
 Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
'''

from esercizio_09_01_import import Restaurant

rest_1 = Restaurant("La Pergola", "cucina italiana")
rest_2 = Restaurant("Il Pagliaccio", "cucina francese e italiana")
rest_3 = Restaurant("Acquolina", "cucina italiana")

print("Ristoranti famosi a Roma:\n")
rest_1.describe_restaurant()
rest_1.open_restaurant()

print("")
rest_2.describe_restaurant()
rest_2.open_restaurant()

print("")
rest_3.describe_restaurant()
rest_3.open_restaurant()


