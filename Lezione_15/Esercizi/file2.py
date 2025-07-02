import json

PATH: str = "Lezione_15/Esercizi/config3.json"
mode: str = "r"

with open(PATH, mode = mode) as file:
    data_diz: dict = json.load(file)

data_diz["kjlfglk34lkjk35kj53"] = {"nome":"Anna", "cognome": "Rossi", "eta": 20}

with open(PATH, mode="w") as file:
    json.dump(data_diz, file, indent=4)


