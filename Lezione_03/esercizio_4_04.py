'''
4-4. One Million: Make a list of the numbers from one to one million, and then use 
a for loop to print the numbers. (If the output is taking too long, 
stop it by pressing CTRL-C or by closing the output window.)
'''

#esercizio 4-4
print("\n Esercizio 4-4 \n")

list_num: list = []

print("\nversione con ciclo for\n")
for i in range(1,1000001):
    list_num.append(i)
print(list_num)

print("\nVersione con while\n")
i:int = 1
while i <= 1000000:
    list_num.append(i)
    i += 1
print(list_num)