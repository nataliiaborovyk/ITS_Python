'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. 
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, 
and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, 
and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
'''

print("\n Esercizio 4-11 \n")

pizza: list = ["Margherita", "Marinara", "Napoletana"]

friend_pizzas: list = pizza.copy()

nuova_pizza: list = ["Capricciosa"]

pizza += nuova_pizza

friend_pizzas.insert(len(friend_pizzas), "4 formaggi")

print("My favourite pizzas are: ")
for i in pizza:
    print(i)

print("\nMy friends's favourite pizzas are: ")
for j in friend_pizzas:
    print(j)