'''
4-8. Cubes: A number raised to the third power is called a cube. For example, 
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes 
(that is, the cube of each integer from 1 through 10), and use a for loop 
to print out the value of each cube.
'''

#esercizio 4-8
print("\n Esercizio 4-8 \n")

print("\nVersione for\n")
list_cub: list = []
for i in range(1,11):
    i = i**3
    list_cub.append(i)
    print(i)

print("\nVersione while\n")
list_cub: list = []
i:int = 1
while i <= 10:
    list_cub.append(i**3)
    i += 1
print(*list_cub)
    


