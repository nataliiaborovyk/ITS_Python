'''
Sistema di Prenotazione Cinema
Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, 
ognuna con un diverso film in programmazione. Gli utenti possono vedere quali film sono disponibili
 e prenotare posti per un determinato spettacolo.
Classi:
- Film: Rappresenta un film con titolo e durata.
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, 
   posti totali, posti prenotati.
   Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili.
      Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
- Cinema: Gestisce le operazioni legate alla gestione delle sale.
   Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti.
      Restituisce un messaggio di stato.
Test case:
    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.
'''

class Cinema:
    
    def __init__(self) -> None:
        self.saleDisponibili: list = []
    
    def aggiungi_sala(self, *sale: "Sala"):
        for sala in sale:
            if sala not in self.saleDisponibili:
                self.saleDisponibili.append(sala)

    def menu_film(self):
        for sala in self.saleDisponibili:
            if sala.getFilmAttuale():
                titolo = sala.getFilmAttuale()
                num = sala.getNumId()
                disp = sala.posti_disponibili()
                print(f"\nSala {num} \nFilm: \"{titolo}\" \nNumero posti disponibili: {disp}")
                
    
    def prenota_film(self, titolo_film: str, num_posti: int):
        if num_posti > 0:
            risultato: bool = False 
            for sala in self.saleDisponibili:
                film = sala.getFilmAttuale()
                if film and film.getTitolo().lower() == titolo_film.lower():
                    risultato = True
                    if sala.posti_disponibili() > num_posti:
                        sala.prenota_posti(num_posti)
                        result: bool = True
                        print(f"Stato di prenotazione: {result}. Hai prenotato {num_posti} per il film: {titolo_film}")
                    else: 
                        result: bool = False
                        print(f"Stato di prenotazione: {result}. Non ci sono {num_posti} diponibili per il film {titolo_film}, per il monento abbiamo solo {sala.posti_disponibili()} posti diponibili" )
                    return   #serve per uscire (interrompere il ciclo for)
            if not risultato:
                print(f"Film \"{titolo_film}\" non è disponibile al cinema")
        else:
            print(f"Error, numero dei posti deve essere maggiore di 0")
    


class Sala:
    
    def __init__(self) ->None:
        self.numId: int = 0
        self.filmAttuale: Film = None
        self.postiTot: int = 0
        self.postiPrenotati:int = 0
 
    def setNumId(self, numId: int) -> None:
        if numId > 0:
            self.numId = numId
        else:
            print(f"Error, Non si puo assegnare {numId} come numero identificatico della sala, il numero deve eseere maggiore di 0")

    def getNumId(self):
        return self.numId

    def setFilmAttuale(self, film: "Film") -> None:
        self.filmAttuale = film

    def getFilmAttuale(self):
        return self.filmAttuale

    def setPostiTot(self, numPostTot:int) -> None:
        self.postiTot = numPostTot

    def prenota_posti(self, num_posti: int) -> str:
        if num_posti <= 0:
            return f"Error, numero dei posti {num_posti} non valido"
        
        if self.posti_disponibili() - num_posti < 0:
            result: bool = False
            return f"Stato di prenotazione: {result}.   Nella Sala {self.numId} purtroppo non ci sono {num_posti} liberi per il film {self.filmAttuale.getTitolo()} ma solo {self.posti_disponibili()}"           
        
        self.postiPrenotati += num_posti
        result: bool = True
        return f"Stato di prenotazione: {result}.   Hai prenotato {num_posti} posti"

    def posti_disponibili(self) -> int:
        return self.postiTot - self.postiPrenotati
    
    def __str__(self) -> str:
        if self.filmAttuale:
            return f"Sala: {self.numId}, Film attuale: \"{self.filmAttuale}\", numero posti disponibili: {self.posti_disponibili()} "
        return "Nessun film in programmazione"

class Film:
    
    def __init__(self) -> None:
        self.titolo: str = ""
        self.durata: int = 0

    def setTitolo(self, titolo: str) -> None:
        self.titolo = titolo

    def setDurata(self, durata: int) -> None:
        if durata < 0:
            raise ValueError("La durata deve essere > 0")
        self.durata = durata

    def getTitolo(self) -> str:
        return self.titolo   

    def getDurata(self) -> int:
        return self.durata 

    def __str__(self) -> str:
        return f"Film: \"{self.titolo}\" dura {self.durata} minuti"
    



    
if __name__ == "__main__":
    
    print("\n     Class Film")
    
    f1: Film = Film()
    print(f"\ntest: {f1}")
    f1.setTitolo("Alice al mare")
    f1.setDurata(90)
    print(f"Atributi aggiornati: {f1}")

    f2: Film = Film()
    f2.setTitolo("Alice in montagna")
    f2.setDurata(60)
    print(f"Atributi aggiornati: {f2}")


    print("\n    Class Sala")
   
    s1=Sala()
    print(f"\ntest: {s1}")
    s1.setNumId(1)
    s1.setNumId(-3)
    s1.setFilmAttuale(f1)
    s1.setPostiTot(50)
    print(f"Atributi aggiornati: {s1}")
    print(f"Posti disponibili: {s1.posti_disponibili()}")
    print(s1.prenota_posti(24))
    print(f"Posti disponibili: {s1.posti_disponibili()}")
    print(f"Provo a prenotare 30 posti\n" , s1.prenota_posti(30))

    s2=Sala()
    print(f"\ntest: {s2}")
    s2.setNumId(2)
    s2.setFilmAttuale(f2)
    s2.setPostiTot(20)
    print(f"\Atributi aggiornati: {s2}")
    print(s2.prenota_posti(5))
    print(f"Posti disponibili: {s2.posti_disponibili()}")
    print(f"Provo a prenotare 32 posti")
    print(s2.prenota_posti(32))


    print("\n    Class Cinema")
    
    c1:Cinema = Cinema()
    c1.aggiungi_sala(s1, s2)
    c1.menu_film()
    print(f"\nPosti disponibili: {s1.posti_disponibili()}")
    c1.prenota_film("alice al mare", 5)
    print(f"Posti disponibili: {s1.posti_disponibili()}")
    print("Provo prenotare 60 posti")
    c1.prenota_film("alice al mare", 60)
    print("Provo prenotare -2 posti")
    c1.prenota_film("alice al mare", -2)
    c1.prenota_film("Alice e Marco", 60)    