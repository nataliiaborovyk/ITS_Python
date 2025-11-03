def ricerca(l:list[int], n:int) -> bool:
    d: int = len(l)
    s: int = 0
    while s < d:
        m: int = (d - s) // 2 + s
        if n == l[m]:
            return True
        elif n < l[m]:
            d = m
        elif n > l[m]:
            s = m + 1  # +1 serve per far finire ciclo while s < d, cosi s cresce e se n non c'è il ciclo finisce
    return False
