'''
Pioggia di Lettere

Le pergamene si coprono di incisioni: 
conta quante volte ogni simbolo riappare, ignorando le macchie. 
Applica `letter_count(text)` per conteggiare solo lettere in minuscolo, 
escludendo tutto il resto. 
Mantieni la firma e promuovi i test.
'''

def letter_count(text: str) -> dict[str,int]:
    lettere: str = "abcdefghijklmnopqrstuvwxyzèòàù"
    text = text.lower()
    diz:dict = {}
    for i in text:
        if i in lettere:
            if i in diz:
                diz[i] += 1
            else:
                diz[i] = 1
    return diz


# alternative

from collections import Counter
import string  # per string.ascii_lowercase

def letter_count(text: str) -> dict[str, int]:
    text = text.lower()
    letters = set(string.ascii_lowercase)  # membership O(1)
    return dict(Counter(ch for ch in text if ch in letters))


def letter_count(text: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for ch in text.lower():
        if ch.isalpha():               # tutte le lettere (anche accentate)
            out[ch] = out.get(ch, 0) + 1
    return out
