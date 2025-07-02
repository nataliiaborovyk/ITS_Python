'''
1. Copy the code and print the age of bob (using the dot notation)
2. Create an if-statement that prints the name of the oldest of the two Persons
3. Create three other Persons. Make a list called people with all 5 Persons.
4. Make a loop that finds and prints the youngest person’s name
'''

print("\n   Esercizio 1 da slide")

class Person:

    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)


        # 1. Print the age of bob (using the dot notation)
print(f"\nEta di Bob: {bob.age}")


        # 2. Create an if-statement that prints the name of the oldest of the two Persons
if alice.age > bob.age:
    print(f"{alice.name } è piu grande")
elif alice.age < bob.age:
    print(f"{bob.age}  è piu grande")
else:
    print("Hanno eta uguale")


        # 3. Create three other Persons. Make a list called people with all 5 Persons.
marco = Person("Marco C", 36)
federico = Person("Federico H", 27)
leonardo = Person("Leonardo P", 29)


        # 4. Make a loop that finds and prints the youngest person’s name
people:list = [alice, bob, marco, federico, leonardo]
p_min = people[0]

for p in people:
    if p.age < p_min.age:
        p_min = p
   
print(f"{p_min.name} è piu giovane")
