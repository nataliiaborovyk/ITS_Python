'''
4-6. Odd Numbers: Use the third argument of the range() function to make a list 
of the odd numbers from 1 to 20. Use a for loop to print each number.
'''

#esercizio 4-6
print("\n Esercizio 4-6 \n")

list_disp: list = []
for i in range(1,21,2):
    list_disp.append(i)
print(*list_disp)


list_disp: list = []
i = 1
while i <= 20:
    print(i)
    i+=2