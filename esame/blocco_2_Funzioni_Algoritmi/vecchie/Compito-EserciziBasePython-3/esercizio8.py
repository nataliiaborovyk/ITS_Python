# Chiede all'utente di inserire 5 numeri
numeri = []

# Itera 5 volte
for i in range(5):
    # Chiede all'utente di inserire un numero
    num = int(input(f"Inserisci un numero tra 1 e 30 ({i+1}/5): "))
    
    # Controlla che il numero sia nel range corretto
    while num < 1 or num > 30:
        # Se il numero non è nel range corretto, chiede all'utente di reinserirlo
        print("Numero non valido! Deve essere tra 1 e 30.")
        num = int(input(f"Inserisci un numero tra 1 e 30 ({i+1}/5): "))
    
    # Aggiunge il numero alla lista
    numeri.append(num)

# Stampa il grafico a barre
print("Grafico a barre:")

# Itera su ogni numero
for num in numeri:
    # Stampa un numero di asterischi pari al numero
    print("*" * num)
