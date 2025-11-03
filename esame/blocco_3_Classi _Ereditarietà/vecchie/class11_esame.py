'''
Classe AppointmentScheduler - PUNTI 2
Progetta una classe AppointmentScheduler per gestire un insieme di appuntamenti.
Attributi:
○ appointments: dict[str, dict]: il dizionario appointments contiene
tutti gli appuntamenti. In dettaglio, la chiave è un app_id (stringa) e il valore
è un altro dizionario che per ogni appuntamento ha le seguenti coppie chiave,
valore:
■ Chiave: str = "data" e Valore: str = “Una data
dell'appuntamento…”
■ Chiave: str = "programmato": e Valore: bool = True oppure
False
Funzioni:
○ schedule_appointment(app_id: str, data: str) -> dict |
str
Se app_id esiste già: restituisci "Errore: appuntamento esiste già.", altrimenti
aggiungi il nuovo appuntamento (con programmato=True) e restituisci un
dizionario con il solo appuntamento appena creato.
○ reschedule_appointment(app_id: str, nuova_data: str) ->
dict | str
Se non esiste restituisci: "Errore: appuntamento non trovato.", altrimenti
aggiorna la data e restituisci un dizionario con il solo appuntamento
aggiornato.
○ cancel_appointment(app_id: str) -> dict | str
Se non esiste restituisci: "Errore: appuntamento non trovato.", altrimenti
imposta programmato=False e restituisci un dizionario con il solo
appuntamento aggiornato.
○ remove_appointment(app_id: str) -> dict | str
Se non esiste restituisci: "Errore: appuntamento non trovato.", altrimenti
rimuovi e restituisci un dizionario con il solo appuntamento rimosso.
○ list_appointments() -> list[str]
Restituisce la lista di tutti gli app_id.
○ get_appointment(app_id: str) -> dict | str
Restituisce il dict dell'appuntamento o "Errore: appuntamento non trovato."
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