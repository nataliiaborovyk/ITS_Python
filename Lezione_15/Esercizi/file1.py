import json

# PATH: str = "Lezione_15/Esercizi/config1.json"
# mode: str = "r"

# with open(PATH, mode=mode) as file:
#     mio_diz: dict = json.load(file)
#     print(mio_diz)


PATH:str = "Lezione_15/Esercizi/creato_dump.json"
mode:str = "w"

with open(PATH, mode=mode) as file:
    nuovo_diz: dict = {"k1":"v1", "k2":"v2","k3":"v3"}
    json.dump(nuovo_diz, file, indent=4)