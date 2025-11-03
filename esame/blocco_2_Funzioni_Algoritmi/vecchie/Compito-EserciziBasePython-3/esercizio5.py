# Chiede all'utente di inserire un numero
euro:int = int(input("Quanti euro sei disposto a spendere: "))
# Salva il valore iniziale di euro
euro_print:int = euro

# Inizializza il contatore delle barrette di cioccolato
choco:int = 0

# Inizializza il contatore dei buoni
buono_sconto:int = 0 

# Calcola il numero di barrette di cioccolato che si possono comprare e i buoni rimanenti
while euro != 0.00:
    # compra una barretta
    choco += 1
    # spendi 1 euro
    euro -= 1 
    # aggiungi un buono sconto
    buono_sconto +=1
    # se hai 6 buoni
    if buono_sconto == 6:
        # aggiungi una barretta gratuita 
        choco +=1 
        # reimposta i buono_sconto a 0, questo perchè le barrette gratuite non contegono buoni sconto
        buono_sconto = 0

print(f"Con {euro_print} euro posso comprare {choco} barrette di cioccolato.\nBuoni rimanenti: {buono_sconto}")