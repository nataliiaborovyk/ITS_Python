def printListBackward(l: list) -> None:
    # se la lista è vuota, stampa la stringa vuota
    if not l:
        print("")
    # altrimenti, stampa l'ultimo carattere
    else:
        print(l[-1])

        # richiama printListBackward ricorsivamente, considerando gli elementi della lista l, 
        # dall'elemento in posizione 0 fino all'ultimo elemento escluso, quindi, fino al penultimo elemento.
        printListBackward(l[:-1])

l: list[int] = [1, 2, 3, 4, 5]
printListBackward(l)

l: list[str] = ["Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"]
printListBackward(l)