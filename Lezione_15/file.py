import json

# PATH: str = "Lezione_15/config.json"     #PATH costante
# mode: str = "r"

# with open(PATH, mode=mode) as file:
#     config: dict = json.load(file)
#     print(config)

#     nome_applicazione: str = config["chiave"]
#     print(nome_applicazione)

# PATH: str = "Lezione_15/main.json"
# mode: str = "w"

# with open(PATH, mode=mode) as file:
#     nuovo_diz:dict = {"nome": "2040", "versione": "1.2.3.4", "OS": "Andoid 16.1.0"}
    
#     json.dump(nuovo_diz, file, indent=4)
    
PATH: str = "Lezione_15/config.json"
mode: str = "w"

with open(PATH, mode="r") as file:
    diz_aggiorn: dict = json.load(file)

diz_aggiorn["chiave"] = "vecchio"

with open(PATH, mode="w") as file:
        
    json.dump(diz_aggiorn, file, indent=4)