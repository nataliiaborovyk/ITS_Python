'''
Exercise 4: Print multiplication table of a given number
'''
num:int = int(input("Inserisci il numero: "))

for i in range(1, 11):
    print(num*i)

i:int = 1
while i < 11:
    print(num*i)
    i += 1