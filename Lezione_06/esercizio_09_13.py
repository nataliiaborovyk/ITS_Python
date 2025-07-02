'''
Dice: Make a class Die with one attribute called sides, which has a default value of 6. 
Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
'''
from random import randint

class Die:

    def __init__(self, sides:int = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides), end=" ")

    
die_6:Die = Die()

for i in range(10):
    die_6.roll_die()

print("")

die_10:Die = Die(10)

for i in range(20):
    die_10.roll_die()