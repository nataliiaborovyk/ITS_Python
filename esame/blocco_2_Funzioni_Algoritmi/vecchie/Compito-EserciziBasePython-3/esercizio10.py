numeri = [] # lista dei numeri inseriti
    
# Chiede all'utente di inserire numeri fino a quando non inserisce 0
while True:
    numero = int(input("Inserisci un numero (0 per terminare): "))
    
    # Se l'utente inserisce 0, esce dal ciclo
    if numero == 0:
        break

    # Aggiunge il numero alla lista
    numeri.append(numero)
    
somma_pari = 0 # somma dei numeri pari
dispari = [] # lista dei numeri dispari

# Calcola la somma dei numeri pari e aggiorna la lista dei numeri dispari    
for n in numeri:
    # Se il numero è pari, aggiungilo alla somma dei numeri pari
    if n % 2 == 0:
        somma_pari += n
    else: # Altrimenti, aggiungilo alla lista dei numeri dispari
        dispari.append(n)
    
# Calcolo della media numeri dispari
if len(dispari) > 0: # Se ci sono numeri dispari, calcola la media dei numeri dispari
    media_dispari = sum(dispari) / len(dispari)
else:
    # Altrimenti, imposta la media a 0
    media_dispari = 0

frequenze = {} # dizionario delle frequenze

# Calcola le frequenze dei numeri
for num in numeri:
    # Se il numero non è presente nel dizionario, aggiungilo con frequenza 1
    if num not in frequenze:
        frequenze[num] = 1
    else: # Altrimenti, incrementa la frequenza del numero
        frequenze[num] += 1


max_freq = max(frequenze.values()) # Trova il numero più frequente
numeri_frequenti = [] # lista dei numeri più frequenti

# Aggiungi alla lista dei numeri più frequenti tutti i numeri con frequenza massima
for num, freq in frequenze.items(): # per ogni numero e la sua frequenza
    if freq == max_freq: # Se la frequenza è quella massima, aggiungi il numero alla lista
        numeri_frequenti.append(num)

# Output risultati
print(f"Somma dei numeri pari: {somma_pari}")
print(f"Media dei numeri dispari: {media_dispari}")
print(f"Numero più frequente: {numeri_frequenti} ({max_freq} volte)")