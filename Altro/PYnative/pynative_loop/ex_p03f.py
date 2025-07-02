#Exercise 3: Calculate sum of all numbers from 1 to a given number

n:int = int(input("Inserisci il numero: "))

sum:int = 0
for i in range(n+1):
    sum += i
print(sum)
