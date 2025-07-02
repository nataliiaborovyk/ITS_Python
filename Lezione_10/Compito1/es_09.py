'''
Si scriva una funzione in Python che simuli una palla che rimbalza calcolando la sua altezza da terra in centimetri per ogni secondo,
 a mano a mano che il tempo passa su un orologio simulato.
Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.
Dopo ogni secondo, il valore dell'altezza cambia, aggiungendo al valore corrente dell'altezza il valore della velocità corrente;
 poi, il valore della velocità viene modificato, sottraendo 96 al valore della velocità corrente.

 Dunque, dopo ogni secondo, si ha che
altezza = altezza + velocità
velocità = velocità - 96.
 
 Se il nuovo valore che si ottiene per l'altezza è inferiore a 0, 
 si deve moltiplicare altezza e velocità per -0.5 per simulare il rimbalzo. Dunque, per il rimbalzo, si avrà che
altezza= altezza*-0,5 
velocità=velocità*-0,5.
Ci si fermi al quinto rimbalzo.
 
 Per ogni secondo, la funzione deve stampare il tempo trascorso e l'altezza a cui si trova la palla in quel determinato secondo.
Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
 "Tempo: 0 Altezza: 0"
 
 Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
 "Tempo: 4 Rimbalzo!"

 For example:
Test 	Result
rimbalzo()
Tempo: 0 Altezza: 0.0
Tempo: 1 Altezza: 100.0
Tempo: 2 Altezza: 104.0
Tempo: 3 Altezza: 12.0
Tempo: 4 Rimbalzo!
Tempo: 5 Altezza: 88.0
Tempo: 6 Altezza: 230.0
Tempo: 7 Altezza: 276.0
Tempo: 8 Altezza: 226.0
Tempo: 9 Altezza: 80.0
Tempo: 10 Rimbalzo!
Tempo: 11 Altezza: 81.0
Tempo: 12 Altezza: 250.0
Tempo: 13 Altezza: 323.0
Tempo: 14 Altezza: 300.0
Tempo: 15 Altezza: 181.0
Tempo: 16 Rimbalzo!
Tempo: 17 Altezza: 17.0
Tempo: 18 Altezza: 172.5
Tempo: 19 Altezza: 232.0
Tempo: 20 Altezza: 195.5
Tempo: 21 Altezza: 63.0
Tempo: 22 Rimbalzo!
Tempo: 23 Altezza: 82.75
Tempo: 24 Altezza: 245.0
Tempo: 25 Altezza: 311.25
Tempo: 26 Altezza: 281.5
Tempo: 27 Altezza: 155.75
Tempo: 28 Rimbalzo!
'''

def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0

    while rimbalzi < 5:
               
        if altezza >= 0:
            print(f"Tempo: {tempo} Altezza: {altezza}")
            altezza += velocita
            velocita -= 96
        else: 
            print(f"Tempo: {tempo} Rimbalzo!")
            altezza *= -0.5
            velocita *= -0.5
            rimbalzi += 1

        tempo += 1

rimbalzo()

    