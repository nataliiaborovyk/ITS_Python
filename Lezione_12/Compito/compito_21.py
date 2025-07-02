class MovieCatalog:

    '''
    Attributi della classe Movie Catalog
    self.cattalog:dict[str, list[strt]]
    '''
    
    def __init__(self) -> None:
        self.setCatalog()

#metodi getter ritorna il valore del attributo self.catalog
    def getCatalog(self) -> dict[str, list[str]]:
        return self.catalog()
    
#metogi setter mermette inizializare l'attributo dself.catalog
    def setCatalog(self) -> None:
        self.catalog: dict[str, list[str]] = {}

#metodi per visualizare i detagli
    def __str__(self) -> str:
        string:str = "Catalogo:"
        
        if self.catalog:
            for key, value in self.catalog.items():
                temp_string:str = "\n" + str(key) + ": " + str(value)
                string = string + temp_string
        return string
    
        #return str(self.catalog)
#metodo che aggiunge una lista di film di uno specifico registra al catalogo
    def add_movies(self, director_name:str, movies: list[str]) -> None:
        #chek seil registra è valido
        if not director_name:
            print("Registra non è valido")
        elif not movies:
            print("La lista dei film non puo essere vuota")
        else:
            #se il registra è presente nel catalogo
            if director_name in self.catalog:
                #aggiungere la lista movies al catalogo
                for movie in movies:
                    #controlare che il film sia stato gia aggiunto nel catalogo
                    #dizionario[key] -> valore (lista dei film di un certo regista)
                    #self.catalog[director_name] le film dei registra director_name
                    if movie in self.catalog[director_name]:
                        print(f"Il film {movie} è gia presente nel catalogo")
                    #se il film non è presente
                    else:
                        self.catalog[director_name].append(movie)
            #se il registra non è presnte nel catalogo
            else:
                self.catalog[director_name] = movies


#metodo remuve movie che elimina film e anche rigistra se è vuoto

    def remove_movie(self, director_name:str, movies:str) -> None:
        if not director_name:
            print("Registra non è valido")
        elif not movies:
            print("La lista dei film non puo essere vuota")
        else:
            #dobiavo vedere se il regista +è presentr nrl catalogo: se si vediamo se movie sta nella sua lista
            if director_name in self.catalog and movies in self.catalog[director_name]:
            #if director_name in self.catalog:
                #for movie in movies:
                    #if movie in self.catalog[director_name]:
                self.catalog[director_name].remove(movies)
            #o self.catalog.pop[director_name]
            if not self.catalog[director_name]:
                del self.catalog[director_name]
            

    #il metodo che ritorna la lista dei film
    def list_directors(self) -> list[str]:
        if self.catalog:
            return list(self.catalog.keys())
        #se dizionario è vuoto
        else:
            return f"Non ci sono registri nel catalogo perche catalogo è vuoto"

                
    #metodo che dato un registra restituisce tutti i film da esso èprodotti
    def get_movies_by_director(self, director_name) -> list[str]:
        if not director_name:
            print("Il redistra non è valido")
        else:
            #controllo se il registra è in catalogo
            if director_name in self.catalog:
                return self.catalog[director_name]
            #se il registra non è in catalogo
            else:
                return f"il registra {director_name} non è in catalogo!"
                
    def search_movies_by_title(title):
        pass

