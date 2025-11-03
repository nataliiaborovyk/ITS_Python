def isValid(x: int) -> bool:
    # verifica se x è un istanza di int o float e nel caso in cui sia float, usa la funzione is_integer() dei float, ovvero 
    # verifica che x sia un numero intero ma scritto come float (ovvero 3.0) e, infine, verifica se x sia >=0
    return ( isinstance(x, int) or (isinstance(x, float) and x.is_integer()) ) and x >= 0

def insertValidNumber() -> int:
    x: int

    
    # controlla se il numero inserito è valido 
    while True:

        try:
            # in questo modo posso considerare validi interi espressi come float, ad esempio 3.0
            x = float(input("Inserisci un numero intero positivo: "))
            if isValid(x):
                break
            else:
                print("Il numero inserito non è valido!")
        except ValueError:
            print("Devi inserire un numero intero! Riprova!")
        
    return int(x)

if __name__ == "__main__":

    x: int = insertValidNumber()
    occ: int = 0
    pos: int = 0
    seq: list[int] = []
    somma: int = 0

    print("Digitare Sequenza!")
    # inserire una sequenza di numeri interi positivi che termina con 0
    while True:
        # digitare un numero valido
        n: int = insertValidNumber()

        # se il numero è valido aggiungerlo alla lista seq.
        seq.append(n)

        # aggiorniamo le occorrenze di x 
        if n == x :
            occ += 1
            # salviamo la posizione della prima occorrenza di x
            if occ == 1:
                pos = seq.index(n)
        
       
        # sommiamo tutti i numeri diversi da x
        else:
            somma = somma + n
        
        # se il numero inserito è 0 termina la sequenza
        if n == 0:
            break
    
    # mostrare i risultati

    # stampare la lista
    print("Hai inserito la sequenza: ", *seq)

    # stampare le occorrenze di x
    if occ == 1:
        print(f"Il numero {x} compare {occ} volta nella sequenza!")
    else:
        print(f"Il numero {x} compare {occ} volte nella sequenza!")
    
    # stampare la posizione della prima occorrenza di x
    print(f"Il numero {x} compare per la prima volta in posizione {pos} nella sequenza")

    # stampare la somma dei numeri diversi da x:
    print(f"La somma dei numeri diversi da x e' {somma}")
    
