from film import Film
from sala import Sala


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
    