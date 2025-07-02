from movie import Movie
from customer import Customer

class VideoRentalStore:

    def __init__(self, movies: dict[str, Movie] = None, customers: dict[str, Customer] = None) -> None:
        self._movies =  movies if movies is not None else {}
        self._customers = customers if customers is not None else {}

    def add_movie(self, movie_id: str, title: str, director: str) -> None: 
        if movie_id not in self._movies:
            m: Movie = Movie(movie_id, title, director)
            self._movies[movie_id] = m
        else:
            print(f"Il film con ID {movie_id} esiste già")

    def register_customer(self, customer_id: str, name: str) -> None: 
        if customer_id not in self._customers:
            c:Customer = Customer(customer_id, name)
            self._customers[customer_id] = c
        else:
            print(f"Il cliente con ID {customer_id} è già registrato")

    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        if customer_id in self._customers and movie_id in self._movies:
            self._customers[customer_id].rent_movie(self._movies[movie_id])
        else:
            print("Cliente o film non trovato")

    def return_movie(self, customer_id: str, movie_id: str) -> None: 
        if customer_id in self._customers and movie_id in self._movies:
            self._customers[customer_id].return_movie(self._movies[movie_id])
        else:
            print("Cliente o film non trovato")

    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        if customer_id in self._customers:
            return self._customers[customer_id]._rented_movies
        else: 
            print("Cliente non trovato")
            return []
        
    def __str__(self) -> str:
        if self._movies:
            elenco1:str = " \n".join(str(i) for i in self._movies.values())
        else:
            elenco1 = "Nessun film registrato"
       
        if self._customers:
            elenco2:str =  " \n".join(str(i) for i in self._customers.values())
        else:
            elenco2 = "Nessun utente registrato"
        
        return f"\nFilm\n{elenco1} \nUtenti\n{elenco2}"
       
    
if __name__ == "__main__":
    
    m1:Movie = Movie("2345", "Bil", "Rossi")

    c1:Customer = Customer("6554", "Nat")

    v:VideoRentalStore = VideoRentalStore()
    print(v)

    v.add_movie("3322", "Aventura", "Verdi")
    print(v)

    v.register_customer("645", "Anna")
    print(v)

    v.rent_movie("645", "3322")
    print(v)

    print(v.get_rented_movies("645"))

    v.return_movie("645", "3322")
    print(v)

    print(v.get_rented_movies("645"))