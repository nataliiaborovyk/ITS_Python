'''
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
Think of five names, and use them as keys in your dictionary. 
Think of a favorite number for each person, and store each as a value in your dictionary. 
Print each person’s name and their favorite number. 
For even more fun, poll a few friends and get some actual data for your program.
'''

#esercizio_6-2
print(" \n   Esercizio_6-2\n")

mydict1: dict[str, int] = { 
    "Anna":7, 
    "Marco":17, 
    "Giuseppe":88, 
    "Feserica":25}

for k, v in mydict1.items():
    print(f"A {k} piace numero {v}")