'''
4-2. Animals: Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. 
You could print a sentence, such as Any of these animals would make a great pet!
'''


#esercizio 4-2
print("\n Esercizio 4-2 \n")

animals: list = ["Dog", "Cat", "Parrot"]

for i in animals:
    print(i)

for i in animals:
    print(f"A {i} would make a great pet")

print("Any animal og our list would make a great pet!")