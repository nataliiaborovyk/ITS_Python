
'''
Esercizio 3C-5. Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età 
di un utente in un dizionario. Il nome, il ruolo e l'età devono essere inseriti in input 
dall'utente stesso. Il programma deve determinare il livello di accesso ai servizi 
in base al ruolo e all'età dell'utente secondo questo schema:
- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"
'''

#Esercizio 3C-5
print("\n Esercizio 3C-5\n")

diz:dict ={}

diz["Nome"] = input("Inserici il nome dell'utente: ").title()
diz["Ruolo"] = input("\nInserici il ruolo dell'utente: ").title()
diz["Eta"] = int(input("\nInserisci l'eta del utente: "))

for k, v in diz.items():
    print(f"\n {k}: {v}")

if diz["Eta"] >= 18:
    match diz:
        case {"Nome":name, "Ruolo":"Admin"}:
            print(f"\n{name} ha accesso completo a tutte le funzionalità\n")
        case {"Nome":name, "Ruolo":"Moderatore"}:
            print(f"\n{name} può gestire i contenuti ma non modificare le impostazioni\n")
        case {"Nome":name, "Ruolo":"Ospite"}:
            print(f"\n{name} accesso ristretto! Solo visualizzazione dei contenuti\n")
        case _:
            print(f"\n Attenzione! Ruolo non riconsciuto! Accesso Negato!\n")
else:
    print(f"\n Accesso limitato! Alcune funzionalità sono bloccate")