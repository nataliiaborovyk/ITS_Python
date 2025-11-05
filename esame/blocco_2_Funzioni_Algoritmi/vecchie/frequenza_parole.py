
import string

def parole_uniche(frase:str):
    diz:dict[str,int] = {}
    puntegiatura:str = string.punctuation
    frase_pul:str = frase.lower()
    tockens:list[str] = frase_pul.split()
    for t in tockens:
        tp:str = t.strip(puntegiatura)
        if not tp:
            continue
        elif tp not in diz:
            diz[tp] = 1
        else: 
            diz[tp] += 1
    return diz
        
