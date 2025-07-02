'''
1-2. Si scriva un programma che dimostri le funzionalità dell'operatore % effettuando le seguenti attività:

    Memorizzare un numero in virgola mobile nella variabile x.
    Calcolare x%2.0 e memorizzare il risultato nella variabile y.
    Visualizzare in maniera distinta x e y.

Si esegua il programma con valori positivi e negativi di x. Che cosa cambia nel comportamento 
dell’applicazione quando i valori di x sono positivi o negativi?
'''

#esercizio_2
print("\n   Esercizio 2\n")

x:float = 6.57
division:float = x / 2.0
floor_division:float = x // 2.0
modulo:float = x % 2.0 

print(f"x = {x}")
print(f"Divisione {x} / 2.0 = {division}")
print(f"Divisioni_interi {x} // 2.0 = {floor_division}")
print(f"Resto della divisione: \n{x} % 2.0 = {x} - (2.0 * ({x}//2.0)) =\n\
= {x} - (2.0 * ({floor_division})) = {modulo}")