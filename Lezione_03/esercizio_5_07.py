'''
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write 
a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of 
fruit is in your list. If the fruit is in your list, the if block should p
rint a statement, such as You really like Apples!
'''

#esercizio 5-7
print("\n Esercizio 5-7 \n")

fruits: list[str] = ["mela", "arancio", "melone", "melograno","fragole", "cocomero"]
favoruite_fruits: list[str] = ["arancio" , "melone", "mela"]

for i in range(len(fruits)):
    if fruits[i] in favoruite_fruits:
         print(f"\nYou really like {fruits[i]} ")
    else:
         print(f"\nYou don't like {fruits[i]}")


