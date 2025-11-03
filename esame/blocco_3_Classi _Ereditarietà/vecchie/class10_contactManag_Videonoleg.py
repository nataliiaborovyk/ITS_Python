'''
Classi
Sviluppa un sistema per la gestione dei contatti in Python che permetta agli utenti di
creare, modificare, e cercare contatti basati sui numeri di telefono. Il sistema dovrà
essere capace di gestire una collezione (dizionario) di contatti e i loro numeri di telefono.
1. Classe ContactManager:
Gestisce tutte le operazioni legate ai contatti.
Attributi:
● contacts: dict[str, list[str]] - Dizionario che ha per chiave il nome del contatto e per
valore una lista di numeri di telefono. I numeri di telefono sono espressi
sottoforma di stringa.
Metodi:
● create_contact(name: str, phone_numbers: list[str]): Crea un nuovo contatto,
aggiungendolo al dizionario contacts con il nome specificato e una lista di numeri
di telefono. Restituisce un nuovo dizionario con il solo contatto appena creato o il
messaggio di errore "Errore: il contatto esiste già." se il contatto esiste già.
● add_phone_number(contact_name: str, phone_number: str): Aggiunge un numero
di telefono al contatto specificato. Restituisce un nuovo dizionario con il solo
contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il
contatto non esiste oppure "Errore: il numero di telefono esiste già." se il numero
di telefono è già presente per il contatto specificato.
● remove_phone_number(contact_name: str, phone_number: str): Rimuove un
numero di telefono dal contatto specificato. Restituisce un nuovo dizionario con il
solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se
il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il
numero di telefono non esiste per il contatto specificato.
● update_phone_number(contact_name: str, old_phone_number: str,
new_phone_number: str): Sostituisce un numero di telefono con un altro nel
contatto specificato. Restituisce un nuovo dizionario con il solo contatto
aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non
esiste oppure "Errore: il numero di telefono non è presente." se il numero di
telefono non esiste per il contatto specificato.
● list_contacts(): Ritorna una lista di tutte le chiavi all'interno del dizionario
contacts.
● list_phone_numbers(contact_name: str): Mostra i numeri di telefono di un
contatto specifico. Restituisce la lista dei numeri di telefono o il messaggio di
errore "Errore: il contatto non esiste." se il contatto non esiste.
● search_contact_by_phone_number(phone_number: str): Trova e restituisce tutti i
contatti che contengono un determinato numero di telefono. Restituisce una lista
di tutte le chiavi all'interno del dizionario contacts che hanno il numero
specificato tra i valori oppure il messaggio di errore "Nessun contatto trovato con
questo numero di telefono." se nessun contatto contiene il numero di telefono.
Progettare un sistema di videonoleggio con i seguenti requisiti:
1. Classe Movie:
Attributi:
● movie_id: str - Identificatore di un film.
● title: str - Titolo del film.
● director: str - Regista del film.
● is_rented: boolean - Booleano che indica se il film è noleggiato o meno.
Metodi:
● rent(): Contrassegna il film come noleggiato se non è già noleggiato. Se il film
non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio "Il
film '{self.title}' è già noleggiato."
● return_movie(): Contrassegna il film come restituito. Se il film è già noleggiato
imposta is_rented a False, altrimenti stampa il messaggio "Il film '{self.title}' non è
stato noleggiato da questo cliente."
2. Classe Customer:
Attributi:
● customer_id: str - Identificativo del cliente.
● name: str - Nome del cliente.
● rented_movies: list[Movie] - Lista dei film noleggiati.
Metodi:
● rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già
stato noleggiato, altrimenti stampa il messaggio "Il film '{movie.title}' è già
noleggiato."
● return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già
presente, altrimenti stampa il messaggio "Il film '{movie.title}' non è stato
noleggiato da questo cliente."
3. Classe VideoRentalStore:
Attributi:
● movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore
l'oggetto Movie.
● customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per
valore l'oggetto Customer.
Metodi:
● add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel
videonoleggio se non è già presente, altrimenti stampa il messaggio "Il film con
ID '{movie_id}' esiste già."
● register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel
videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente
con ID '{customer_id}' è già registrato."
● rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."
● return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."
● get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film
noleggiati dal client (customer.rented_movies) se il cliente esiste nel
videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una
lista vuota
'''