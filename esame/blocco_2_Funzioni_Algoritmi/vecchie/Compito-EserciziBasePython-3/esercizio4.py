somma:int = 0 # Somma dei numeri interi
counterInt:int = 0  # Contatore dei numeri interi inseriti

massimo:float = float('-inf') # Inizializzo il massimo a -infinito
minimo:float = float('inf') # Inizializzo il minimo a +infinito

while True:
    # Chiedo all'utente di inserire un numero
    n:float = float(input("Inserire un numero: "))

    # Controllo se l'utente ha inserito un numero negativo per terminare il programma
    if n < 0:
        print("Programma terminato.")
        break
    # Se il numero è positivo
    else:
        # Controllo se il numero è intero
        if n.is_integer():
            # Incremento il contatore dei numeri interi e aggiungo il numero alla somma
            counterInt += 1
            # Aggiungo il numero alla somma dei numeri interi
            somma += int(n)

        # Controllo se il numero è maggiore o minore del massimo e del minimo
        if n > massimo:
            massimo = n # Aggiorno il massimo
        if n < minimo: 
            minimo = n # Aggiorno il minimo

# Calcolo e stampo la media dei soli numeri interi, solo se sono stati inseriti numeri interi
if counterInt > 0:
    media:float = somma / counterInt
    print(f"La media dei soli numeri interi vale: {media}")

# Controllo se il massimo e il minimo sono stati aggiornati rispetto ai valori iniziali
if massimo != float('-inf') and minimo != float('inf'):
    # Stampo il massimo e il minimo
    print(f"Valore massimo inserito: {massimo}")
    print(f"Valore minimo inserito: {minimo}")
