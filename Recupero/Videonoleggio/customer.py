from movie import Movie

class Customer:

    def __init__(self, customer_id: str, name: str) -> None:
        self._customer_id = customer_id
        self._name = name
        self._rented_movies: list[Movie] = []

    def rent_movie(self, movie: Movie) -> None: 
        if not movie._is_rented:
            movie.rent()
            self._rented_movies.append(movie)
        else:
            print(f"Il film {movie._title} è già noleggiato")

    def return_movie(self, movie: Movie) -> None: 
        if movie in self._rented_movies:
            movie.return_movie()
            self._rented_movies.remove(movie)
        else:
            print(f"Il film {movie._title} non è stato noleggiato da questo cliente")

    def __str__(self):
        if self._rented_movies:
            elenco: str = ", ".join(i._title for i in self._rented_movies)
        else:
            elenco = "Nessun film noleggiato"
        return f"ID: {self._customer_id}, Nome: {self._name}, Rented Movies: {elenco}"

if __name__ == "__main__":
    m1:Movie = Movie("2345", "Bil", "Rossi")
    print(m1)
    m1.rent()
    print(m1)
    m1.return_movie()
    print(m1)

    c1:Customer = Customer("6554", "Nat")
    print(c1)
    c1.rent_movie(m1)
    print(c1)
    print(m1)
    c1.return_movie(m1)
    print(c1)
    print(m1)