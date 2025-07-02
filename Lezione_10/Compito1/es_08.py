'''
Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi (ore, minuti e secondi)
 e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta 
 (le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).
Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, 
ovvero sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.
Definire, poi, la funzione chiamata time_difference che prende come argomento due orari,
 entrambi espressi mediante ore, minuti e secondi. 
 La funzione time_difference deve usare la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, 
 entrambi contenuti entro un ciclo dell'orologio di 12 ore.
Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.
For example:
Test 	Result
print(time_difference(1, 0, 0, 3, 15, 30))    8130
print(time_difference(0, 0, 0, 12, 0, 0))    43200
'''

def seconds_since_noon(ore:int, minuti:int, secondi:int) -> int:
    
    time_sec:int = (ore * 60 * 60) + (minuti * 60) + secondi
    time_sec_full:int = (12 * 60 * 60) 
   
    while True:
        if time_sec > time_sec_full:
            time_sec -= time_sec_full
        else:
            break

    return time_sec

def time_difference(ore1:int, min1:int, sec1:int, ore2:int, min2:int, sec2:int):
    
    x = seconds_since_noon(ore1, min1, sec1)
    y = seconds_since_noon(ore2, min2, sec2)
    
    if x > y:
        return x - y
    else:
        return y - x

print(time_difference(1, 0, 0, 3, 15, 30))   
print(time_difference(0, 0, 0, 12, 0, 0)) 