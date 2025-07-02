class Restaurant:

    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant \"{self.restaurant_name}\": {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant \"{self.restaurant_name}\" is open")