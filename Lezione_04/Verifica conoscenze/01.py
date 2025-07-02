'''
Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account 
(attivo/non attivo). L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" 
e l'account è attivo. La funzione ritorna "Accesso consentito" oppure "Accesso negato".
print(check_access("admin", "12345", True))   Result  Accesso consentito
print(check_access("admin", "54321", True))           Accesso negato
'''

def check_access(username: str, password: str, is_active: bool) -> str:
    # cancella ... è definisci il tipo di dato per password, successivamente cancella pass e scrivi il tuo codice
    if username == "admin" and password == "12345" and is_active == True:
        return "Accesso consentito"
    else:
        return "Accesso negato"
    
 	

print(check_access("admin", "12345", True))    #Accesso consentito
print(check_access("admin", "12345", False))     #Accesso negato
print(check_access("user", "12345", True))       #Accesso negato
print(check_access("admin", "54321", True))      #Accesso negato
print(check_access("admin", "54321", False))     #Accesso negato

