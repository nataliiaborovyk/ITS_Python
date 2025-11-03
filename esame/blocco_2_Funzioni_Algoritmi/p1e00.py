'''
### B2.I.1 — Staircase Ways (DP base)

**Task.** `count_ways(n: int) -> int`: numero di modi per salire `n` gradini, 
potendo fare passi da 1 o 2, **ma non sono consentite due mosse “2” consecutive**.
**Esempio.** `n=3` → sequenze valide: `1+1+1`, `1+2`, `2+1` → `3`. 
(La sequenza `2+2` non è valida per `n=4` a causa della regola.)
'''

def count_ways(n: int) -> int:
    # Se n < 0 non ha senso
    if n < 0:
        return 0
    # Caso base: 0 gradini → 1 modo (non fare niente)
    if n == 0:
        return 1

    # Tabella per memorizzare i risultati
    # a[i] = quanti modi ci sono di arrivare al gradino i finendo con un passo da 1.
    # b[i] = quanti modi ci sono di arrivare al gradino i finendo con un passo da 2.
    a = [0] * (n + 1)
    b = [0] * (n + 1)

    # Condizioni iniziali
    a[1] = 1        # per arrivare a 1 → solo passo da 1
    b[1] = 0
    if n >= 2:
        a[2] = 1    # (1+1)
        b[2] = 1    # (2)

    # Riempimento tabella dal terzo gradino in poi
    # Le celle a[i] e b[i] non contengono passi, ma conteggi (numeri di modi).
    for i in range(3, n + 1):    # indici i (0, 1, 2, …, n) rappresentano i gradini.
        a[i] = a[i-1] + b[i-1]    # puoi sempre fare un passo da 1
        b[i] = a[i-2]             # puoi fare un 2 solo se prima NON era 2
                                  # (cioè solo se arrivi da a[i-2])

    # Totale modi per arrivare a gradino n
    return a[n] + b[n]
