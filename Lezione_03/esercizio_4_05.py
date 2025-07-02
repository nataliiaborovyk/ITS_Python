'''
4-5. Summing a Million: Make a list of the numbers from one to one million, and then 
use min() and max() to make sure your list actually starts at one and ends at one million. 
Also, use the sum() function to see how quickly Python can add a million numbers.
'''

#esercizio 4-5
print("\n Esercizio 4-5 \n")

list_num: list = []

for i in range(1,1000001):
    list_num.append(i)

print(f"Il numero min = {min(list_num)} \nIl numero max = {max(list_num)} \nLa somma dei numeri tra {min(list_num)} e {max(list_num)} = {sum(list_num)}")