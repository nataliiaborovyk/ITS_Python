'''
### B1.I.5 — Tuple Arithmetic Window (liste, tuple, slicing)

**Task.** Data `values: list[int]` e una finestra `w: int (w>0)`, 
produrre una **lista di tuple** `(start_index, end_index, window_sum, window_avg)` 
per ogni segmento contiguo di ampiezza `w`.
**Output.** Lista di tuple ordinate per `start_index`. Se `w > len(values)`, restituisci `[]`.
**Nota.** Usa slicing e `sum` con attenzione alla complessità.
'''

# divido in segmenti separati
def arithmetic(values:list[int], w:int) -> list[tuple]:
    if len(values) < w:
        return []
    fin:list = []
    for index in range(0,len(values),w):
        wind:list = values[index:index+w]
        w_sum = sum(wind)
        w_avg = w_sum / w
        fin.append((index, index+w-1, w_sum, w_avg))
    return fin

print(arithmetic([1,2,4,6,7,8], 2))


# divido in segmenti sovraposti
def arithmetic2(values:list[int], w:int) -> list[tuple]:
    if len(values) < w:
        return []
    fin:list = []
    for index in range(0,len(values)-w+1):
        wind:list = values[index:index+w]
        w_sum = sum(wind)
        w_avg = w_sum / w
        fin.append((index, index+w-1, w_sum, w_avg))
    return fin

print(arithmetic2([1,2,4,6,7,8], 2))