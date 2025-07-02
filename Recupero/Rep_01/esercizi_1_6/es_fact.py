def fattoriale(n:int) -> int:
    prod: int = 1
    for i in range(1,n+1):   #for i in range(n)
        prod *= i                 #prod *= n-i
    return prod
print(fattoriale(5))

def fattoriale2(n:int) -> int:
    prod: int = 1
    for i in range(n):  
        prod *= n - i                 
    return prod
print(fattoriale2(5))
