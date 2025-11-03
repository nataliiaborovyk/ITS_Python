def proDict() -> dict[tuple[int, int], int]:

    # dizionario d 
    d: dict[tuple[int], int] = {}

    # riempire il dizionario d 

    # tutti i valori di x sono dati da 
    for x in range(1, 101):
        # tutti i valori di y sono dati da 
        for y in range(2, 89, 2):

            d[(x,y)] = x * y 
    

    return d

if __name__ == '__main__':

    d: dict[tuple[int, int], int] = proDict()

    print(f"d[(13, 88)]: {d[(13, 88)]}")
    print(f"d[(83, 56)]: {d[(83, 56)]}")
    print(f"d[(71, 44)]: {d[(71, 44)]}")
