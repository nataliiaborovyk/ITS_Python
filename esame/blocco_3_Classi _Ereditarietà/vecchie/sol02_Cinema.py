class MovieCatalog:
    # Costruttore della classe MovieCatalog
    def __init__(self) -> None:
        # Dizionario che contiene i nomi dei registi come chiavi e la lista dei film come valori
        self.catalog: dict[str, list[str]] = {}

    # Metodo per aggiungere un film al catalogos
    def add_movie(self, director_name: str, movies: list[str]) -> dict[str,list[str]]:
        # Se il regista non è già presente nel catalogo, lo aggiungo al dizionario
        if director_name not in self.catalog:
            # La chiave è il nome del regista, il valore è la lista dei film
            self.catalog[director_name] = movies
            # Restituisco un dizionario con il nome del regista come chiave e la lista dei film come valore
        else:
            # Se il regista è già presente nel catalog
            for movie in movies:
                # Se il film non è già presente nella lista dei film del regista, lo aggiungo
                if movie not in self.catalog[director_name]:
                    # Aggiungo il film alla lista dei film del regista
                    self.catalog[director_name].append(movie)
            
        # Restituisco un dizionario con il nome del regista come chiave e la lista dei film come valore
        return {director_name: self.catalog[director_name]}

    # Metodo per rimuovere un film dal catalogo
    def remove_movie(self, director_name: str, movie_name: str) -> dict[str,list[str]]:
        # Se il regista è presente nel catalogo e il film è presente nella lista dei film del regista
        if director_name in self.catalog and movie_name in self.catalog[director_name]:
            # Rimuovo il film dalla lista dei film del regista
            self.catalog[director_name].remove(movie_name)
            # Se la lista dei film del regista è vuota, rimuovo il regista dal catalogo
            if not self.catalog[director_name]:
                # Rimuovo il regista dal catalogo
                del self.catalog[director_name]

        # Restituisco il catalogo aggiornato
        return self.catalog

    # Metodo per visualizzare i registi presenti nel catalogo
    def list_directors(self) -> list[str]:
        # Restituisco la lista dei nomi dei registi
        return list(self.catalog.keys())

    # Metodo per visualizzare i film di un regista
    def get_movies_by_director(self, director_name: str) -> list[str] | str:
        # Restituisco la lista dei film del regista
        # Se il regista esiste nel dizionario
        if director_name in self.catalog:
            # Restituisco la lista dei film del regista
            return self.catalog[director_name]
        else:
            # Se il regista non esiste, restituisco un messaggio di errore
            return f"Il resgitsta '{director_name}' non è presente nel catalogo."

   # Metodo per cercare un film per titolo
    def search_movies_by_title(self, title: str) -> dict[str, list[str]] | str:
        result: dict[str, list[str]] = {}  # Dizionario per memorizzare il risultato
        # Itera per ogni regista e lista di film nel catalogo
        for director, movies in self.catalog.items():
            # Lista temporanea per memorizzare i film che corrispondono al titolo cercato
            matching_movies = []
            # Controlla ogni film sotto questo regista
            for movie in movies:
                # Se il titolo cercato è contenuto nel titolo del film, aggiungilo alla lista temporanea
                if title.lower() in movie.lower():
                    matching_movies.append(movie)
            # Se abbiamo trovato dei film corrispondenti, aggiungili al risultato
            if matching_movies:
                result[director] = matching_movies

        # Se abbiamo trovato dei film corrispondenti, restituiscili
        if result:
            # Se ci sono risultati, ritornali
            return result
        else:
            # Se non ci sono risultati, ritorna un messaggio che indica che non sono stati trovati film
            return f"Nessun film trovato con il titolo '{title}'"
                
# Esempio di utilizzo:
catalog = MovieCatalog() # Creo un catalogo di film
catalog.add_movie("Steven Spielberg", ["I Goonies", "Ritorno al futuro", "Casper"]) # Aggiungo il regista e dei film al catalogo
catalog.add_movie("Quentin Tarantino", ["Pulp Fiction", "Kill Bill", "Django Ritorno"]) # Aggiungo un altro regista e dei film al catalogo
catalog.add_movie("Steven Spielberg", ["E.T. l'extra-terrestre", "Indiana Jones e l'ultima crociata"]) # Aggiungo altri film ad un regista già presente nel catalogo
print(catalog.remove_movie("Steven Spielberg", "Casper")) # Rimuovo un film dal catalogo
print(catalog.list_directors()) # Visualizzo i registi presenti nel catalogo
print(catalog.get_movies_by_director("Steven Spielberg")) # Visualizzo i film di un regista
print(catalog.search_movies_by_title("ritorno")) # Cerco un film esistente per titolo
print(catalog.search_movies_by_title("potter")) # Cerco un film non in catalogo per titolo
