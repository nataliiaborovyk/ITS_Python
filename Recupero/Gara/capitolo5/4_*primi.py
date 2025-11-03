'''
Fessure Prime

Per separare i metalli nobili, cataloga i numeri primi fino alla soglia. 
Implementa `primes_up_to(n)` restituendo tutti i primi **≤ n** ordinati; 
per `n` < `2`, `[]`. 
Mantieni la firma e promuovi i test.
'''

def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    primi: list = []
    for i in range(2, n+1):
        if i == 2:
            primi.append(i)
            continue
        if i % 2 == 0:
            continue
        cont :int = 0
        sqrt:int = int(i**0.5) + 1
        for k in range(3, sqrt, 2):
            if i % k == 0:
                cont = 1
                break
        if cont == 0:
            primi.append(i)
    return primi

