'''
Exercise 4 (Folder 9 ex_4.py)
1. Write a new class called Food, it should have name, price and
description as attributes.
2. Instantiate at least three different foods you know and like.
3. Create a new class called Menu, it should have a list (of Foods) as attribute.
__init__ should take a list of Foods as optional parameters (default=[])
4. Create a addFood() and removeFood() for the Menu
5. Create a few new Food instances. Add each to the Menu using the respective
Method.
6. Add a method printPrices() that list all items on the Menu with their
prices.
7. Add a Menu method getAveragePrice() that returns the average Food
price of the Menu
'''
print("\n   Esercizio 4 dalle slide")

        # 1. Write a new class called Food, it should have name, price and description as attributes.

class Food:

    def __init__(self, name:str, price:float, description:str):
        self.name = name
        self.price = price
        self.description = description
    
    def printInfo(self):
        print(f"{self.name} is {self.description} and cost {self.price}$")
        

        # 2. Instantiate at least three different foods you know and like.
caffe = Food("Caffè", 10, "nice drink in the morning")
pizza = Food("Pizza", 5, "better then sandwich")
cake = Food("Cake", 7, "good desert")

caffe.printInfo()
pizza.printInfo()
cake.printInfo()

lista_food:list = [caffe, pizza, cake]

        # 3. Create a new class called Menu, it should have a list (of Foods) as attribute. 
        # __init__ should take a list of Foods as optional parameters (default=[])

class Menu:

    def __init__(self, lista_food:list = []):
        self.lista_food = lista_food

    def addFood(self, val):
        self.lista_food.append(val)

    def removeFood(self, val):
        index = self.lista_food.index(val)
        elem = self.lista_food.pop(index)
    
    def printPrices(self):
        for i in self.lista_food:
            print(f"{i.name} costa {i.price}")

    def getAveragePrice(self):
        sum = 0
        for i in self.lista_food:
            sum += i.price
        if len(self.lista_food) == 0:
            print("Error")
        else:
            media = sum / len(self.lista_food)
        return media
        

        # 4. Create a addFood() and removeFood() for the Menu
        # 5. Create a few new Food instances. Add each to the Menu using the respective Method.

pane = Food("Pane", 2, "Mangiamo sempre volentieri")
mela = Food("Mela", 1, "frutta fa bene alla salute")

product = Menu(lista_food)
product.addFood(pane)
product.addFood(mela)
product.removeFood(pizza)


        # 6. Add a method printPrices() that list all items on the Menu with their prices.
print("")
product.printPrices()

        # 7. Add a Menu method getAveragePrice() that returns the average Food price of the Menu
media = product.getAveragePrice()
print(f"La media dei prezzi: {media}")