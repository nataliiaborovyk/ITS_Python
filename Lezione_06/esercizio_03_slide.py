'''
Exercise 3 (Folder 9 ex_3.py)
Given is the class Animal. For each task, test your changes!
1. Create two realistic instances of Animals
2. Print the name of each object
3. Change the amount of legs of one object using the dot notation
4. Add a method setLegs() to set the legs of an object and repeat task 3 but
this time using the method.
5. Add a method getLegs() to return the amount of legs
6. Add a method named printInfo that prints all attributes of the Animal
'''

print("\n   Esercizio 3 dalle slide")

class Animal:

    legs_start = 0

    def __init__(self, type:str, name:str, legs:int):
        self.type = type
        self.name = name
        self.legs = legs
        self.legs_start = legs

    def setLegs(self, newLegs):
        self.legs = newLegs

    def getLegs(self):
        self.legs = self.legs_start

    def printInfo(self):
        print(f"{self.name} is a {self.type} and has {self.legs} legs")

        
        # 1. Create two realistic instances of Animals
cat = Animal("cat", "Asia", 4)
parrot =Animal("parrot", "Bil", 6)

        # 2. Print the name of each object
print(f"{cat.name} has {cat.legs} legs")
print(f"{parrot.name} has {parrot.legs} legs")

        # 3. Change the amount of legs of one object using the dot notation
parrot =Animal("parrot", "Bil", 2)
print(f"\nUpdate: {parrot.name} has {parrot.legs} legs")

        # 4. Add a method setLegs() to set the legs of an object a
        # and repeat task 3 but this time using the method.
parrot.setLegs(4)
print(f"{parrot.name} change legs to {parrot.legs}")

        # 5. Add a method getLegs() to return the amount of legs
parrot.getLegs()
print(f"{parrot.name} started with {parrot.legs} legs\n")

        # 6. Add a method named printInfo that prints all attributes of the Animal
cat.printInfo()
parrot.printInfo()
