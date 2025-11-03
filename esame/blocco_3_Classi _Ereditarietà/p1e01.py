class LibraryItem:
    def __init__(self, item_id: str, title: str) -> None:
        self.item_id: str = item_id
        self.title: str = title
        self.available: bool = True  # per chiarezza tipologica

    def describe(self) -> str:
        stato = "Disponibile" if self.available else "Non disponibile"
        return f"id: {self.item_id} | titolo: {self.title} | {stato}"

    def borrow(self) -> bool:
        if self.available:
            self.available = False
            return True
        return False

    def return_item(self) -> None:
        self.available = True


class Book(LibraryItem):
    def __init__(self, item_id: str, title: str, author: str) -> None:
        super().__init__(item_id, title)  # inizializza la classe base prima
        self.author: str = author

    def describe(self) -> str:
        stato = "Disponibile" if self.available else "Non disponibile"
        return f"id: {self.item_id} | titolo: {self.title} | autore: {self.author} | {stato}"


class Dvd(LibraryItem):
    def __init__(self, item_id: str, title: str, duration_min: int) -> None:
        super().__init__(item_id, title)
        self.duration_min: int = duration_min  

    def describe(self) -> str:
        stato = "Disponibile" if self.available else "Non disponibile"
        return f"id: {self.item_id} | titolo: {self.title} | durata: {self.duration_min} min | {stato}"
