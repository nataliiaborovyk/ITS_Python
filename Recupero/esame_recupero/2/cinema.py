'''
Sistema di Gestione di un Cinema - PUNTI 2
Implementa tre classi interagenti per gestire biglietti di film.
Classe Ticket:
Attributi
○ ticket_id: str
○ movie: str
○ seat: str
○ is_booked: bool
Metodi:
○ book() -> None: se "is_booked" è False, lo imposta a True; altrimenti
stampa "Il biglietto per '{self.movie}' posto '{self.seat}' è già prenotato."
○ cancel() -> None: se "is_booked" è True, lo imposta a False;
altrimenti stampa "Il biglietto per '{self.movie}' posto '{self.seat}' non risulta
prenotato."
Classe Viewer:
Attributi
○ viewer_id: str
○ name: str
○ booked_tickets: list[Ticket]
Metodi:
○ book_ticket(ticket: Ticket) -> None: se "ticket.is_booked"
è False, aggiunge "ticket" a "booked_tickets" e chiama
"ticket.book()"; altrimenti stampa "Il biglietto per '{ticket.movie}' non è
disponibile."
○ cancel_ticket(ticket: Ticket) -> None: se "ticket" è in
"booked_tickets", lo rimuove e chiama "ticket.cancel()"; altrimenti
stampa "Il biglietto per '{ticket.movie}' non è stato prenotato da questo
spettatore."
Classe Cinema:
Attributi
○ tickets: dict[str, Ticket]
○ viewers: dict[str, Viewer]
Metodi:
○ add_ticket(ticket_id: str, movie: str, seat: str) -> None:
se "ticket_id" esiste: stampa "Il biglietto con ID '{ticket_id}' esiste già.",
altrimenti aggiunge un nuovo "Ticket".
○ register_viewer(viewer_id: str, name: str) -> None: se
"viewer_id" esiste: stampa "Lo spettatore con ID '{viewer_id}' è già
registrato.", altrimenti aggiunge un nuovo "Viewer".
○ book_ticket(viewer_id: str, ticket_id: str) -> None: se
entrambi esistono, invoca "viewer.book_ticket(ticket)"; altrimenti
stampa "Spettatore o biglietto non trovato."
○ cancel_ticket(viewer_id: str, ticket_id: str) -> None: se
entrambi esistono, invoca "viewer.cancel_ticket(ticket)"; altrimenti
stampa "Spettatore o biglietto non trovato."
○ list_available_tickets() -> list[str]: restituisce la lista di
"ticket_id" con "is_booked == False".
○ list_viewer_bookings(viewer_id: str) -> list[str] | str:
■ se lo spettatore esiste, restituisce lista di \"ticket_id\" prenotati;
■ Altrimenti restituisce "Errore: spettatore non trovato."
'''

class Ticket:

    def __init__(self, ticket_id: str, movie: str, seat: str, is_booked = False) -> None:
        self.ticket_id = ticket_id
        self.movie = movie
        self.seat = seat
        self.is_booked = is_booked

    def book(self) -> None:
        if self.is_booked == True:
            raise ValueError(f" il biglietto per {self.movie} posto {self.seat} è gia prenotato")
        self.is_booked = True

    def cancel(self) -> None:
        if self.is_booked == False:
            raise ValueError(f" il biglietto per {self.movie} posto {self.seat} è gia prenotato")
        self.is_booked = False       


class Viewer:
    def __init__(self, viewer_id: str, name:str, booked_tickets: list[Ticket] = None) -> None:
        self.viewer_id = viewer_id
        self.name = name
        self.booked_tickets = booked_tickets or None

    def book_ticket( self, ticket: Ticket) -> None:
        if ticket.is_booked == True:
            print(f" il biglietto per {ticket.movie} non è disponibile")
        else:
            self.booked_tickets.append(ticket)
            ticket.book()

    def cancel_ticket(self, ticket:Ticket) -> None:
        if ticket not in self.booked_tickets:
            print(f"Il biglietto per '{ticket.movie}' non è stato prenotato da questo spettatore")
        else:
            self.booked_tickets.remove(ticket)
            ticket.cancel()


class Cinema:
    def __init__(self, tickets: dict[str,Ticket]= None, viewers: dict[str, Viewer] = None) -> None:
        self.tickets: dict[str, Ticket] = tickets or {}
        self.viewers: dict[str,Viewer] = viewers or {}

    def add_ticket(self, ticket_id: str, movie: str, seats:str) -> None:
        if ticket_id in self.tickets:
            print(f"Il biglietto con ID '{ticket_id}' esiste già")
        else:
            self.tickets[ticket_id] = Ticket(ticket_id, movie, seats)

    def register_viewer (self, viewer_id, name: str) -> None:
        if viewer_id in self.viewers:
            print(f"Lo spettatore con ID '{viewer_id}' è già registrato.")
        else:
            self.viewers[viewer_id] = Viewer(viewer_id, name)

    def book_ticket(self, viewer_id: str, ticket_id: str) -> None:
        if viewer_id in self.viewers and ticket_id in self.tickets:
            self.viewers[viewer_id].book_ticket(self.tickets[ticket_id])
    
    def cancel_ticket(self, viewer_id:str, ticket_id: str) -> None:
        if viewer_id in self.viewers and ticket_id in self.tickets:
            self.viewers[viewer_id].cancel_ticket(self.tickets[ticket_id])

    def list_available_ticket(self) -> list[str]:
        return [x for x, y in self.tickets.items() if y.is_booked == False ]
    
    def list_viewer_boolings(self, viewer_id:str) -> list[str] | str:
        if viewer_id in self.viewers:
            return [x.ticket_id for x in self.viewers[viewer_id].booked_tickets]
        


def filter_and_concat(num:list[int], main: int) -> str:
    list2 = [str(x) for x in num if x > main]
    return "".join(list2)

