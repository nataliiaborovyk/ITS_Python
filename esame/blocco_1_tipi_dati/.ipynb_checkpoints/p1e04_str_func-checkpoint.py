'''
### B1.I.4 — Tokenize & Join (stringhe)

**Task.** Implementare `normalize_and_join(s: str, sep: str=',') -> str` che:

* rimuove spazi multipli, punteggiatura terminale `.,;:!?` dai token,
* converte tutti i token a **lowercase**,
* elimina token vuoti,
* restituisce una stringa con i token **unici nell’ordine di prima apparizione**, uniti da `sep`.
  **Esempio.** `"  Hello, hello;  WORLD!?  world  "` → `"hello,world"`.
'''

def normalize_and_join(s: str, sep: str =',') -> str:
    s = s.lower()
    punt:str = ".,;:!?"
    for el in punt:
        if el in s:
            s = s.replace(f"{el}", "")
    liat: list = list(set(s.split()))
    fin = f"{sep}".join(liat)
    return fin

print(normalize_and_join("  Hello,    hello;  WORLD!?  world  "))


def normalize_and_join(s: str, sep: str = ',') -> str:
    # 1️⃣ Converti tutta la stringa in minuscolo
    s = s.lower()

    # 2️⃣ Dividi la stringa in token (parole), ignorando spazi multipli
    tokens = s.split()   # "  Hello   world  ".split()  →  ['Hello', 'world']

    # 3️⃣ Lista che conterrà i token "puliti" e unici
    unique_tokens = []

    # 4️⃣ Punteggiatura terminale da rimuovere
    punctuation = ".,;:!?"

    # 5️⃣ Ciclo su ogni parola trovata
    for tok in tokens:
        # Rimuove solo la punteggiatura alla fine della parola (non nel mezzo)
        tok = tok.rstrip(punctuation)

        # Se il token non è vuoto e non è già stato aggiunto, aggiungilo
        if tok != "" and tok not in unique_tokens:
            unique_tokens.append(tok)

    # 6️⃣ Unisci i token finali con il separatore richiesto
    result = sep.join(unique_tokens)
    return result

def norm(s:str, sep=','):
    s=s.lower()
    unic=[]
    token=s.split()
    punt:str = ".,;:!?"
    for i in token:
        i = i.rstrip(punt)
        if i is not "" and i not in unic:
            unic.append(i)
    fin= sep.join(unic)
    return fin

