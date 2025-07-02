'''
Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. 
La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) 
e restituire l'ipotenusa come un float.
Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.
For example:
Test 	Result
print(hypotenuse(3.0, 4.0))   5.0
print(hypotenuse(8.0, 15.0))   17.0
'''
import math
def hypotenuse(a:float, b:float) -> float:
    
    return math.sqrt((a**2 + b**2))

print(hypotenuse(3.0, 4.0))  
print(hypotenuse(8.0, 15.0)) 


x=10
y=3
print(x//y)
print(x%y)