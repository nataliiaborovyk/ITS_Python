# importa modulo per gestire le espressioni regolari
import re

# verifica se una data sequenza sia una sequenza di DNA valida.
# Nota. se la stringa inserita è vuota, la sequenza di DNA non sarà valida
def isDNA(seq: str) -> bool:
    # controlla se l'intera stringa corrisponde al pattern considerato, 
    # ovvero se le lettere che compongolo la stringa seq sono una sequenza di carateeri A,C,G e T.
    # il simbolo + indica una o più occorrenze dell'elemento precedente, ovvero una o più occorrenza dei caratteri [ACGT]
    # r prima delle virgolette sta per raw string, ovvero stringa grezza. Dunque, Python deve interpretare la stringa così come è, nel modo in cui è scritta.
    # Questo significa che i caratteri specifiali come \n, \t non sono interpretati come speciali ma come carattere nornmale.
    # Infatti, "\n" (senza r) indica il carattere di new line
    # metre r "\n" indica proprio i caratteri \n 
    # in questo modo, quando si scrive una regex, se la regex presenta, ad esempio, il carattere \d, Python non processa \d come carattere speciale
    # ma lo lascia così come è in modo da essere interpretato correttamente dalla regex. 
    # senza la r, dovrei scrivere l'operatore della regex in questo modo "\\d", ovvero con il doppio slash

    # Infine, la funzione re.fullmatch() ritorna un oggetto di tipo re.Match, se la sequenza è valida.
    # Se la sequenza non è valida, la funzione re.fullmatch() ritornerà None. 
    # Per questo motivo si va a richiedere nella condizione che se re.fullmatch() non è None
    return re.fullmatch(r"[ACGT]+", seq.upper() ) is not None
    

# restituisce una sequenza di DNA
def insertDNASequence(input_message: str) -> str:
    seq: str = ""
    while True:
        seq = input(input_message)

        # controlla se la sequenza di DNA inserita sia valida
        if isDNA(seq):
            break
        else:
            print("Sequenza DNA inserita non valida!")
    return seq


if __name__ == "__main__":

    # stringa 1 con check
    s1: str = insertDNASequence("Inserire il primo frammento di DNA")

    # stringa 2 on check
    s2: str = insertDNASequence("Inserire il secondo frammento di DNA")

    # algoritmo più lungo
    '''
    # per confrontare le due stringhe s1 e s2, devo utilizzare un ciclo for.
    # per evitare l'out of range, ho bisogno di sapere quale delle due strainghe tra s1 e s2 è la più corta.
    end: int = min(len(s1), len(s2))

    # conta la lunghezza della sequenza
    len_seq: int = 0
    
    for i in range(end):

        # parto dall'ultimo carattere di s1 e scorro s1 verso destra fino a vedere se si riesce a trovare una corrispondenza con il primo carattere 
        # della stringa s2. 
        # se non c'è corrispondenza, passo all'iterazione successiva
        
        # scorri la stringa s1 da destra verso sinistra, mentre scorri la lista s2 da sinistra verso destra.
        # per la stringa s1, parto dall'ultimo carattere e comincio a considerare, per ogni iterazione del ciclo, 
        # una sottostringa di s1 che parte dal carattere in posizione -i-1 e arriva fino alla fine della stringa s1. 
        # s1_substr = s1[-i:]
        # per la stringa s2, parto dal primo carattere e comincio a considerare, per ogni iterazione del ciclo, 
        # una sottostringa di s2 che parte dall'inizio della strainga s2 fino al carattere in posizione i esclusa. 
        # s2_substr = s2[:i]

        # per ogni iterazione ricava s1_substr
        s1_substr: str = ""
        # per ogni iterazione ricava s2_sbustr
        s2_substr = ""

        for j in range(i+1):
            # costruisci s1_substr
            s1_substr = s1_substr + s1[-j-1]
            # costruisci s2_substr
            s2_substr = s2_substr + s2[j]

        
        # ho riempito s1_substring all'incontrario, ovvero il primo carattere di s1_substr è l'ultimo carattere di s1. 
        # io vorrei che l'ultimo carattere di s1_substr sia uguale all'ultimo carattere di s1. 
        # Dunque, per poter leggere la s1_substr correttamente da sinistra verso destra e 
        # per poter confrontare correttamente s1_substr con s2_substr devo invertire s1_substr, ovvero devo leggerla al contrario
        s1_substr = s1_substr[::-1]

        # se poi le due sottostringhe sono uguali, allora ho trovato la corrispondenza. 
        # Dunque, conta la lunghezza della sequenza
        if s1_substr == s2_substr:
            # la lunghezza della sequenza sarà data dalla lunteghezza di una delle due sottostringhe
            len_seq = len(s1_substr)
        
        # se len_seq > 0 e le due sottostringhe non coincidono, significa che abbiamo trovato la lunghezza massima della sequenza.
        # dunque, interrompiamo il ciclo per evitare inutili iterazioni
        if len_seq > 0 and s1_substr != s2_substr:
            break
        
    '''

    # posso ottimizzare il codice lavorando con lo slicing:
    
    # parto dall'ultimo carattere di s1 e scorro s1 verso destra fino a vedere se si riesce a trovare una corrispondenza con il primo carattere 
    # della stringa s2. 
    # se non c'è corrispondenza, passo all'iterazione successiva
    
    # scorri la stringa s1 da destra verso sinistra, mentre scorri la lista s2 da sinistra verso destra.
    # per la stringa s1, parto dall'ultimo carattere e comincio a considerare, per ogni iterazione del ciclo, 
    # una sottostringa di s1 che parte dal carattere in posizione -i-1 e arriva fino alla fine della stringa s1. 
    # s1_substr = s1[-i:]
    # per la stringa s2, parto dal primo carattere e comincio a considerare, per ogni iterazione del ciclo, 
    # una sottostringa di s2 che parte dall'inizio della strainga s2 fino al carattere in posizione i esclusa. 
    # s2_substr = s2[:i]
    # posso quindi lavorare con lo slicing:
    
    # per confrontare le due stringhe s1 e s2, devo utilizzare un ciclo for.
    # per evitare l'out of range, ho bisogno di sapere quale delle due strainghe tra s1 e s2 è la più corta.
    end: int = min(len(s1), len(s2))
    
    # conta la lunghezza della sequenza
    len_seq: int = 0

    for i in range(1, end +1):
        # check delle sottostringhe
        if s1[-i:] == s2[:i]:
            # se le sottostringhe matchano, calcola la lunghezza della sottostringa trovata 
            len_seq = len(s1[-i:])
        
        # se len_seq > 0 e le due sottostringhe non coincidono, significa che abbiamo trovato la lunghezza massima della sequenza.
        # dunque, interrompiamo il ciclo per evitare inutili iterazioni
        if len_seq > 0 and s1[-i:] != s2[:i]:
            break         


    # stampo in output i risultati:

    # stampo s2 sovrapposta a s1, in corrispondenza dell'inizio della sequenza
    # quindi devo stampare spazi fino all'inizio della sequenza di sovrapposizione 
    # e poi stampare s2

    # stampo s1
    print(s1.upper())

    # stampo spazi
    for i in range(len(s1) - len_seq):
        print(" ", end="")

    # stampo s2
    print(s2.upper())

    print(f"\nLa lunghezza massima di sovrapposizione e' {len_seq}")







    
            

    
