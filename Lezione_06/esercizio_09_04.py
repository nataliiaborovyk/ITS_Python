'''
9-4. Number Served: Start with your program from Exercise 9-1. 
- Add an attribute called number_served with a default value of 0. 
- Create an instance called restaurant from this class. 
- Print the number of customers the restaurant has served, and then change this value and print it again. 
- Add a method called set_number_served() that lets you set the number of customers that have been served. 
- Call this method with a new number and print the value again. 
- Add a method called increment_number_served() that lets you increment the number of customers 
who’ve been served. Call this method with any number you like that could represent 
how many customers were served in, say, a day of business. 
'''
print("\n   Esercizio 9 -4")

class Restaurant:

    def __init__(self, restaurant_name:str, cuisine_type:str, number_served:int = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"Restaurant \"{self.restaurant_name}\": {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant \"{self.restaurant_name}\" is open")

    def set_number_served(self, new_number_served:int = 0):
        self.number_served = new_number_served

    def increment_number_served(self, val:int):
        self.number_served += val

        
        # Create an instance called restaurant from this class. number_served default = 0
        
restaurant = Restaurant("La Pergola", "cucina italiana", 50)


        # Print the number of customers the restaurant has served

print(f"\nUsually \"{restaurant.restaurant_name}\" in a day served {restaurant.number_served} customers")


        # change value of number of customers and print it again

restaurant.number_served = 55
print(f"\nYesterday: \"{restaurant.restaurant_name}\" in a day had served {restaurant.number_served} customers")


        # Add a method called set_number_served() that lets you set the number of customers that have been served
        # Call this method with a new number and print the value again
    
restaurant.set_number_served()
print(f"\nNew day: \"{restaurant.restaurant_name}\" had served {restaurant.number_served} customers")

restaurant.set_number_served(5)
print(f"\nAfternoon: \"{restaurant.restaurant_name}\" had served {restaurant.number_served} customers")


        # Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
        # Call this method with any number you like that could represent how many customers were served in a day of business.

restaurant.increment_number_served(14)
print(f"\nUpdate: \"{restaurant.restaurant_name}\" in a day had served {restaurant.number_served} customers")
