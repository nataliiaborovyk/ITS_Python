'''
Ponte delle Spirali

Nella sala delle spirali raccogli le gocce fino all'ultima: 
implementa `range_sum(n)` per sommare da `1` a `n`; 
se il contenitore (`n`) non ha volume (≤ `0`), restituisci `0`. 
Mantieni la firma e lascia che gli esperimenti (i test) riescano.
'''

def range_sum(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return n + range_sum(n-1)