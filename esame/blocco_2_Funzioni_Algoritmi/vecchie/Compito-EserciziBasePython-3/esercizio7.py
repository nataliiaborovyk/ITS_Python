a:list[int] = [10, 20, 30] # lista a
b:list[int] = [40, 50, 60] # lista b
c:list[int] = [] # lista c

n:int = len(a) # lunghezza della lista a

# iterazione su ogni elemento della lista a
for i in range(n):
    # aggiungi alla lista c la somma tra l'elemento i-esimo della lista a e l'elemento (n-1)-i della lista b
    c.append(a[i] + b[(n-1)-i])
    
print(c)