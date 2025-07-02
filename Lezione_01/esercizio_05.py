'''
5. Verifica se un numero è primo
Progetta un algoritmo per determinare se un numero 
intero positivo inserito dall'utente è un numero primo.
'''
# versione 2 seconda diagramma

n:int = int(input("Inserisci il numero positivo: "))
is_prime: bool = True


if n < 2:
    is_prime = False
else:
    div: int = 2
    while True:
        if div <= (n ** (1/2)):
            if n % div == 0:
                
                is_prime = False
                break
            div += 1
        #else: 
         #   is_prime = False
          #  break
if is_prime == True:
    print(f"Il numero {n} è primo")
else:
    print(f"Il numero {n} non è primo")