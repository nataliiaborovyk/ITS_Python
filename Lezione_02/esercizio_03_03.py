'''
3-3. Your Own List: Think of your favorite mode of transportation, 
such as a motorcycle or a car, and make a list that stores several examples. 
Use your list to print a series of statements about these items, 
such as “I would like to own a Honda motorcycle.”
'''

#esercizio_3-3
print("\n esercizio_3-3\n")

mylist3: str = ["Mersedes", "BMW", "Tesla"]
#print(*mylist3)
for i in mylist3:
    print(f"I would like to own a {i} car")
