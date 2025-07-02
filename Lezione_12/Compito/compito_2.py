'''
Sistema di Gestione Catalogo Film 
Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, 
rimuovere e cercare film di un particolare regista. 
Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi della classe:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. 
    Se il regista non esiste, viene creato un nuovo record. 
    Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. 
    Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
    Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata 
       o un messaggio di errore se nessun film contiene la parola cercata nel titolo.
 
Codice driver
    Crea un’istanza della classe MovieCatalog.
    Aggiungi nuovi film e registi.
    Aggiungi film a registi già presenti nel catalogo.
    Rimuovi film dal catalogo.
    Elenca i registi presenti nel catalogo.
    Visualizza film di uno specifico regista.
    Cerca film per parola chiave nel titolo, gestendo il caso con risultati che senza.
'''
import re

class MovieCatalog:

    def __init__(self):
        self.diz:dict[str, list[str]] = {}

    def add_movie(self, director_name:str, movies_name:list[str]):
        for dir,mov in self.diz.items():
            if dir == director_name:
                mov.extend(movies_name)
                return
        self.diz[director_name] = movies_name

    def remove_movie(self, director_name, movie_name):
        if director_name in self.diz:
            if movie_name in self.diz[director_name]:
                self.diz[director_name].remove(movie_name)
                if not self.diz[director_name]:
                    self.diz.pop(director_name)    
            else:
                print(f"\nRegistra {director_name} non ha film {movie_name} nel catalogo")
        else:
            print(f"\nRegistra {director_name} non c'è nel catalogo")

    def list_directors(self):
        print("\nNel catalogo sono presenti seguenti registri: ")
        for director in self.diz.keys():
            print(f"- {director}")

    def get_movies_by_director(self, director_name):
        print(f"\nRegistra {director_name} ha sequenti film: ")
        for director, movie in self.diz.items():
            if director == director_name:
                for film in movie:
                    print(f"- {film}")
                

    def search_movies_by_title(self, title:str):
        print(f"\nLa parola {title} si incontra nel nome di seguenti film: ")
        for director, movie in self.diz.items():
            for film in movie:
                if title.lower() in film.lower():
                    print(f"- {film}, registra {director}")

    def list_all(self):
        print("\nElenco completo dei resisti e loro film nel cataloto")
        for director, movie in self.diz.items():
            print(f"\nRegistra {director}: ")
            for film in movie:
                print(f"-{film}")


c1:MovieCatalog = MovieCatalog()

c1.add_movie("alen", ["Anna", "Maria al mare"])

c1.add_movie("bili", ["Marco va al mare", "Mare azzuro", "Libri"])

c1.add_movie("franco", ["bel mare", "cielo"])

c1.list_directors()

c1.get_movies_by_director("bili")

c1.search_movies_by_title("mare")

c1.remove_movie("bili", "Libri")

c1.remove_movie("alen", "Maria")

c1.list_all()