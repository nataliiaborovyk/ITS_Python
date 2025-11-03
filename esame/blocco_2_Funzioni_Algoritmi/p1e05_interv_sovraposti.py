'''

### **B2.I.5 — Interval Merge & Length (algoritmi su liste)**

**Task.** Data `intervals: list[tuple[int,int]]` con `start ≤ end`, implementa
`merged_total_length(intervals) -> int`
che unisce gli intervalli sovrapposti e calcola la **lunghezza totale coperta**.
**Esempio.**

```
[(1,3), (2,6), (8,10), (10,12)]
→ unione [(1,6), (8,12)]
→ lunghezza totale = 9
```

**Vincolo.** Usa ordinamento e scansione lineare (`for`), nessuna libreria esterna.

'''

def merged_total_length(intervals:list[tuple[int,int]]) -> int:


    if len(intervals) <= 1:
        return intervals
    
    intervals.sort(key=lambda x: x[0])
    
    fin:list = [intervals[0]]

    for suc_int in intervals[1:]:
        ult_int:list = intervals[-1]
        if suc_int[0] < ult_int[1]:
            ult_int[1] = max(ult_int[1], suc_int[1])
        else:
            fin.append(suc_int)
    return fin