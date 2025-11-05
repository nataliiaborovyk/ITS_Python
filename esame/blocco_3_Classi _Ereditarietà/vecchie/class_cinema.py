'''
Sistema di Prenotazione Cinema

Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

Test case:

    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.
 
'''

class Film:

    def __init__(self, titolo:str, durata:int) -> None:
        self.titolo = titolo
        self.durata = durata

    def get_titolo(self) -> str:
        return self.titolo
    
    def get_durata(self) -> int:
        return self.durata
    

class Sala:

    def __init__(self, num_id:int, film_at:Film, posti_tot:int, posti_pren:int = None) -> None:
        self.num_id = num_id
        self.film_at = film_at
        self.posti_tot = posti_tot
        self.posti_pren = posti_pren or 0

    def prenota_posti(self, num_posti:int) -> str:
        if num_posti <= self.posti_disponibili():
            self.posti_pren += num_posti
            print(f'hai prenotato {num_posti} per film {self.film_at.get_titolo()}')
        else:
            print(f'non ci sono {num_posti} disponibili per film {self.film_at.get_titolo()}')

    def posti_disponibili(self) -> int:
        return self.posti_tot - self.posti_pren
    
    def get_film_at(self):
        return self.film_at
    

class Cinema:

    def __init__(self, sale:list[Sala] = None) -> None:
        self.sale = sale or []

    def aggiungi_sala(self, sala:Sala) -> None:
        if sala in self.sale:
            raise ValueError('è gia presnte')
        self.sale.append(sala)

    def prenota_film(self, titolo_film:str, num_posti:int) -> str:
        trovato:bool = False
        for s in self.sale:
            if s.get_film_at().get_titolo() == titolo_film:
                s.prenota_posti(num_posti)
                trovato = True
                break
        if not trovato:
            print(f'non esiste film {titolo_film} nel cinema')

if __name__ == "__main__":

    f1:Film = Film("Anna al mare", 240)
    f2:Film = Film('Gita bella', 120)

    s1:Sala = Sala(1,f1,20)
    s2:Sala = Sala(2,f2,15)

    c:Cinema = Cinema()

    c.aggiungi_sala(s1)
    c.aggiungi_sala(s2)

    c.prenota_film("Anna al mare",5)
    c.prenota_film("Anna al mare",10)
    c.prenota_film("Anna al mare",7)




            

