'''
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life.
 Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.
'''

#esercizio 5-6
print("\n Esercizio 5-6 \n")


age: int = int(input("\nWhat is your age?: "))

if age <= 2:
    print("\nThat the person is a baby!")

elif age > 2 and age < 4:
    print("\nThat the person is a toddler!")
    
elif age >= 4 and age < 13:
    print("\nThat the person is a kid!")

elif age >= 13 and age < 20:
    print("\nThat the person is a teenager!")

elif age >= 20 and age < 65:
    print("\nThat the person is a toddler adult!")

elif age >= 65:
    print("\nThat the person is a elderr!")



match age:

    case age if age <= 2:
        print("\nBaby")
    case age if age > 2 and age < 4:
        print("\nToddler")
    case age if age >= 4 and age < 13:
        print("\nKid")
    case age if age >=13 and age < 20:
        print("\nTeenager")
    case age if age >= 20 and age < 65:
        print("\nAdult")
    case age if age >65:
        print("\nElder")