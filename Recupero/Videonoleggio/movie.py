
class Movie:

    def __init__(self, movie_id: str, title: str, director: str) -> None:
        self._movie_id = movie_id
        self._title = title
        self._director = director
        self._is_rented: bool = False

    def rent(self) -> None:
        if not self._is_rented:
            self._is_rented = True
        else:
            print(f"Il film {self._title} è già noleggiato")

    def return_movie(self) -> None:
        if self._is_rented:
            self._is_rented = False
        else:
            print(f"Il film {self._title} non è stato noleggiato da questo cliente")

    def __str__(self):
        stato = "no" if self._is_rented else "si"
        return f"Id: {self._movie_id}, Titolo: {self._title}, Director: {self._director}, Disponibile: {stato}"

if __name__ == "__main__":
    m1:Movie = Movie("2345", "Bil", "Rossi")
    print(m1)
    m1.rent()
    print(m1)
    m1.return_movie()
    print(m1)
