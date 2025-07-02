'''
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, 
represent the famous person’s name using a variable called famous_person. 
Then compose your message and represent it with a new variable called message. 
Print your message. 
'''

#esercizio_2-6
print("\n esercizio_2-6\n")

name: str = "Lao Tzu"
quote: str = "A journey of a thousand miles begins with\
 a single step"
famous_person:str = "Walt Disney"
message:str = "If you can dream it, you can do it"

name = famous_person
quote = message
print(f"{name} once said, \n \"{quote}\"")

