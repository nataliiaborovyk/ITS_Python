'''
4-7. Threes: Make a list of the multiples of 3, from 3 to 30. 
Use a for loop to print the numbers in your list.
'''

#esercizio 4-7
print("\n Esercizio 4-7 \n")

print("\nVersione for\n")
list_mult3: list = []
for i in range(3,31,3):
    list_mult3.append(i)
print(*list_mult3)

print("\nVersione while\n")
list_mult3: list = []
i: int = 1
while i<=30:
    list_mult3.append(i)
    i += 3
print(*list_mult3)