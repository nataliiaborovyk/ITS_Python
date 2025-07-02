'''
Raffinamento dei requisiti
1. Movimenti Tartaruga
1.1. Passo veloce (50% di probabilità): avanza di 3 quadrati. 1 ≤ i ≤ 5
1.2. Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1. 6 ≤ i ≤ 7
1.3. Passo lento (30% di probabilità): avanza di 1 quadrato. 8 ≤ i ≤ 10

2. Movimenti Lepre
2.1. Riposo (20% di probabilità): non si muove.  1 ≤ i ≤ 2
2.2. Grande balzo (20% di probabilità): avanza di 9 quadrati. 3 ≤ i ≤ 4
2.3. Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.  i = 5
2.4. Piccolo balzo (30% di probabilità): avanza di 1 quadrato. 6 ≤ i ≤ 8
2.5. Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1. 9 ≤ i ≤ 10


3. Regole di gara
  3.1. Inizio gara - stampare 'BANG !!!!! AND THEY'RE OFF !!!!!'
  3.2. Percorso lungo 70 quadratini (rappresentato come una lista)
  3.3. Partenza animali dal 1 quadratino
  3.4. Finish al 70-esimo quadratino
  3.5. Se animale scivola sotto 1 quadratino, va riportato al 1 quadratino
  3.6. Usare  delle variabili per tenere traccia delle posizioni degli animali
  3.7. Dopo ogni secondo del orologio (“tick”) stampare la posizione dei animali 
       3.7.1. Posizione tartaruga - “T”
       3.7.2. Posizione lepre - “H”
       3.7.3. Posizione libera - “_”
       3.7.4. Se posizione tartaruga == posizione lepre - stampare 'OUCH!!!'
  3.8. Dopo la stampa di ogni “tick”, verificate se gli animali hanno raggiunto o superato il quadrato 70.
       3.8.1. Se si, stampare il nome del vincitore e terminare la simulazione
              3.8.1.1. Se vince tartaruga - "TORTOISE WINS! || VAY!!!"
              3.8.1.2. Se vince lepre - "HARE WINS || YUCH!!!"
              3.8.1.3. Se arrivano insieme - IT'S A TIE."
       3.8.2. Se no, simulare il succesivo “tick” del orologio

'''



import random

print("Band!!! And They're off!!!!")

#come si muove la tartaruga

def tartaruga(posizione_t:int = 1):

    i_t: int = random.randint(1,10)

    if 1 <= i_t <= 5:     #Passo veloce 
        posizione_t += 3

    elif 6 <= i_t <= 7:     #Scivolata
        posizione_t -= 6

    elif 8 <= i_t <= 10:      #Passo lento
        posizione_t += 1

    if posizione_t <= 0:
        posizione_t = 0

    elif posizione_t > 70:
        posizione_t = 70
        
    return posizione_t
    

#come si muove la lepre  

def lepre(posizione_l:int = 1):

    i_h: int = random.randint(1,10)
    
    if 1 <= i_h <= 2:   #riposo 20%
        posizione_l += 0 

    elif 3 <= i_h <= 4:  #grande balzo 20%
        posizione_l += 9

    elif 5 == i_h:
        posizione_l -= 12   #grande scivolata 10%

    elif 6 <= i_h <= 8:   #piccolo balzo 30%
        posizione_l += 1

    elif 9 <= i_h <= 10:   #piccolo scivolata 20%
        posizione_l -= 2

    if posizione_l <= 0:
        posizione_l = 0

    elif posizione_l > 70:
        posizione_l = 70
        
    return posizione_l




def gara(quadratini:int = 70):
    tick = 0
    posizione_t = 1
    posizione_l = 1

    while (posizione_t < quadratini) and (posizione_l < quadratini):

        posizione_t = tartaruga(posizione_t)      #aggiorno la posizione dei animali in ogni atterazione
        posizione_l = lepre(posizione_l)
        
        percorso:list = []               #ogni volta creo una nuova lista e aggiungo le posizioni dei animali

        for i in range(quadratini):
            percorso.append("_")

        if posizione_l != posizione_t:
            percorso[posizione_t-1] = "T"      #animali partono dalla posizione 1 e indici della lista cominciano da 0
            percorso[posizione_l-1] = "H"

        else:
            percorso[posizione_l-1] = "OUCH!!!"

        tick += 1

        print(*percorso)

    if posizione_t == quadratini:             #verifico chi prima è arrivato al finish
        print("TORTOISE WINS! || VAY!!!")

    elif posizione_l == quadratini:
        print("HARE WINS || YUCH!!!")

    else:
        print("IT'S A TIE")
    

gara()
    
        

        
