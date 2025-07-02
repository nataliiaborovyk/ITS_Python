def printListaBackward(lista:list[int]):
    if not lista: 
        return   #si ferma qui, non stampa niente peche la lista è vuota
    printListaBackward(lista[1:])
    #stampa il primo elemento della lista del ultima ricorsione cioe [3] poi [2,3] poi [1,2,3]
    print(lista[0])