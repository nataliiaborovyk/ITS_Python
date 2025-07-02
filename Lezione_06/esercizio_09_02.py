'''
9-2. Three Restaurants: Start with your class from Exercise 9-1. 
Create three different instances from the class, and call describe_restaurant() for each instance.
'''
print("\n   Esercizio 9 -2")

from esercizio_09_01 import Restaurant

print("\nAltri 3 ristoranti famosi a Roma:\n")

rest_4 = Restaurant("All'oro", "cucina romana")
rest_4.describe_restaurant()

rest_5 = Restaurant("Acquolina", "cucina mediteranea")
rest_5.describe_restaurant()

rest_6 = Restaurant("Enoteca la Torre Villa Laetitia", "cucina mediteranea")
rest_6.describe_restaurant()
