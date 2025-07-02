from string import ascii_lowercase

def caesar_cypher_decrypt(s: str, key: int) -> str:

    lettere:str = ascii_lowercase
    if key > 26:
        key = key % 26
    frase_nuova:str = ""
    s = s.lower()
    for i in range(len(s)):
        if s[i] in lettere:
            posiz = lettere.index(s[i])
            posiz1 = (posiz - key) % 26
            new_carat = lettere[posiz1]
            frase_nuova += new_carat
        else:
            frase_nuova += s[i]

    return frase_nuova

if __name__ == "__main__":
    print(caesar_cypher_decrypt("ekcq!", 2))
    print(caesar_cypher_decrypt("ekcq!", 28))