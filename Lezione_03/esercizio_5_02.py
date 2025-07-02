'''
5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. 
If you want to try more comparisons, write more tests and add them
to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
'''

#esercizio 5-2
print("\n Esercizio 5-2 \n")


print("\tTests for equality and inequality with strings\n")
caffe: str = "caldo"
print(f'Il caffe è: {caffe}')
print("Is caffe == caldo? I predict is True.")
print(caffe == "caldo\n")

print("Is caffe == freddo? I predict is False.")
print(caffe == "freddo")

print("Is caffe != amaro? I predict is True.")
print(caffe != "amaro")

#Tests using the lower() method

print("\n\tTests using the lower() method\n")
citta: str = "Roma"
print(f'La citta è: {citta}')
print("Is citta.lower() == Roma? I predict is False.")
print(citta.lower() == "Roma")

print("Is citta.lower() == roma? I predict is True.")
print(citta.lower() == "roma")

print("Is name.lower() != ROMA? I predict is True.")
print(citta.lower() != "ROMA")


# Numerical tests involving equality and inequality, greater than and less than, 
# greater than or equal to, and less than or equal to

print("\tNumerical tests\n")

x: int = 10
y: int = 25

print("Is x == y? I predict is False.")
print(x == y)

print("Is x != y? I predict is True.")
print(x != y)

print("Is x > y? I predict is False.")
print(x > y)

print("Is x < y? I predict is True.")
print(x < y)

a: int = 50
b: int = 20

print(f'\na = {a}\nb = {b}\n')
print("Is a >= b? I predict is True.")
print(a >= b)

print("Is a <= b? I predict is False.")
print(a <= b)

print("Is a != b? I predict is True.")
print(a != b, '\n')

# Tests using the and keyword and the or keyword
print("\tTests using the and keyword and the or keyword\n")

x: int = 26
y: int = 40
z: int = 30

print(f'x = {x} \ny = {y}\nz = {z}')
print("\nIs x < y and x > z? I predict is False.")
print('Risultato: ', x < y or x > z,'\n')

print("Is y < z or y > x? I predict is True.")
print('Risultato: ', y < z or y > x,'\n')

print("Is z > x or x > y? I predict is True.")
print('Risultato: ', z > x or x > y,'\n')

print("Is y > z and y < x? I predict is False.")
print('Risultato: ', y > z and y < x,'\n')



#Test whether an item is in a list
print("\tTest whether an item is in a list\n")

animals: list[str] = ["Dog", "Cat", "Parrot"]

print("Is Dog in animals list? I predict is False.")
print('Risultato: ', 'Dog' not in animals, '\n')

print("Is Cat in animals list? I predict is True.")
print('Risultato: ', 'Cat' in animals,'\n')

print("Is Bird in animals list? I predict is False.")
print('Risultato: ', 'Bird' in animals, '\n')
