'''
2. Automazione di un semaforo intelligente
Progettare un algoritmo che simuli il comportamento di un semaforo intelligente. 
Questo sistema deve adattare i tempi di durata (espressi in percentuale) 
del verde in base al numero di veicoli presenti sulle principali direzioni di traffico: 
Nord-Sud ed Est-Ovest. Ogni direzione può ricevere una priorità se il numero di veicoli supera una soglia predefinita.
Requisiti:
    Se il numero di veicoli in una sola direzione supera la soglia (es. 70 veicoli),
      quella direzione riceve un tempo minimo garantito per il verde (es. 60%) 
      e il restante tempo è assegnato all'altra direzione.
    Se entrambe le direzioni superano la soglia, il tempo è equamente suddiviso (50% per ciascuna direzione).
    Se nessuna direzione supera la soglia, il tempo è calcolato proporzionalmente
      al numero totale di veicoli nelle due direzioni.
Stampare la percentuale del tempo assegnato al verde per ciascuna direzione.
'''

nord_sud: int = int(input("Inserisci il numero di veicoli presenti sul traffico Nord-Sud: "))
est_ovest: int = int(input("Inserisci il numero di veicoli presenti sul traffico Est-Ovest: "))
soglia:int = 70

if nord_sud > soglia and est_ovest > soglia:
    time_ns = 50
    time_eo = 50
    
else:
    if nord_sud > soglia:
        time_ns = 60
        time_eo = 40
       
    else:
        if est_ovest > soglia:
            time_ns = 40
            time_eo = 60
            
        else:
            time_ns = (nord_sud / (nord_sud + est_ovest) * 100)
            time_eo = (est_ovest / (nord_sud + est_ovest) * 100)

