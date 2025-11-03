'''
Tamburo dei Multipli

Il reattore risponde a frequenze 3 e 5: usa `sum_multiples(limit)` 
per sommare tutte le letture **< limit** divisibili per `3` o `5`. 
Per `limit` ≤ `0`, restituisci `0`. 
Mantieni la firma e titola i test.
'''

def sum_multiples(limit: int) -> int:
    if limit <= 0:
        return 0
    return sum(i for i in range(1, limit) if i % 3 == 0 or i % 5 == 0)

    