'''
### **B2.I.1 — Staircase Simple (ricorsione base o iterativa)**

**Task.** `count_steps(n: int) -> int`: dato un numero di gradini `n`, 
restituisci il **numero di modi possibili** per salire la scala
 se puoi fare **solo passi da 1 o 2**, **senza nessuna regola speciale**.
**Esempio.** `n = 3` → `1+1+1`, `1+2`, `2+1` → `3`.
**Nota.** Puoi risolvere con ricorsione o con un ciclo `for`,
 ma senza usare tabelle di programmazione dinamica.
'''

def count_steps(n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return count_steps(n-1) + count_steps(n-2) 

'''
ultimo ciclo di ricorsiva sarebbe quando n scende a 2.  
count_steps(1) + count_steps(0) qui n=1 e n=0 . :
 io sono la funzione e chiamo me stessa  diminuendo valore di parametro entro in certo limite. 
 qui partono due rami per  count_steps(n-1)  e per count_steps(n-2). 
 quando un ramo scende a 1 altro puo scendere a 0.
 qui devo fermare discesa per questo scrivo casi basi
'''
