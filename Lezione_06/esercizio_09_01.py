'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, 
and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
'''
print("\n   Esercizio 9 -1\n")

class Restaurant:

    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant \"{self.restaurant_name}\": {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant \"{self.restaurant_name}\" is open")


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


