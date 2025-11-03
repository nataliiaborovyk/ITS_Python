'''
### **B2.I.2 — Compress Runs (run-length custom)**

**Task.** `compress_runs(s: str) -> str`: 
comprimi solo i gruppi consecutivi (run) di caratteri di **lunghezza ≥ 3**, 
scrivendoli nella forma `char{count}`.
Lascia invariati i run di lunghezza 1 o 2.
**Esempio.**
`"aaabbccccd"` → `"aaabbc{4}d"`.
**Vincolo.** Nessuna libreria esterna; usare solo cicli e variabili temporanee.
'''

def compress_runs(s: str) -> str:
    if not s:
        return ""
    fin:list[str] = []
    n = len(s)
    i = 0

    while i < n:
        cont = 1  # 1 perche gia esiste 1 carattere
        j = i + 1

        while j < n and s[i] == s[j]:
            cont += 1
            j += 1
            
        if cont >= 3:
            fin.append(f"{s[i]}{cont}")
        else:
            fin.append(f"{s[i]*cont}")
        i = j

    result = "".join(fin)
    return result


            

