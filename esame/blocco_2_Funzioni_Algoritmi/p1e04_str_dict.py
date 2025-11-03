'''
### **B2.I.4 — Anagram Buckets (dict + funzioni)**

**Task.** `group_anagrams(words: list[str]) -> dict[str, list[str]]`: 
raggruppa insieme tutte le parole che sono **anagrammi** 
tra loro (stesse lettere, in qualunque ordine).
La chiave del dizionario sarà la “firma” dell’anagramma
 (le lettere ordinate in minuscolo).
Mantieni l’**ordine originale** delle parole dentro ogni bucket.
**Esempio.**
`["Roma", "amor", "mora", "Armo"]` →
`{"amor": ["Roma", "amor", "mora", "Armo"]}`.
'''

def group_anagrams(words: list[str]) -> dict[str, list[str]]:

    diz:dict[str, list[str]] = {}
    set_par:set = set()

    for par in words:
        par_min = "".join(sorted(par.lower()))
        set_par.add(par_min)

    for firm in set_par:
        for par in words:
            if firm == "".join(sorted(par.lower())):
                if firm not in diz:
                    diz[firm] = [par]
                else:
                    diz[firm].append(par)
    
    return diz

        