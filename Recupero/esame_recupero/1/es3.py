def filter_and_aquere(num:list[int], soglia:int) -> list[int]:
    lista:list = []
    for i in num:
        if i > soglia and i % 2 == 0:
            lista.append(i**2)
    return lista

    return [i**2 for i in nums if i > soglia and i % 2 == 0 ]