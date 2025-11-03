'''
Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

    Classe Book:
        Attributi:
            book_id: str - Identificatore di un libro.
            title: str - titolo del libro.
            author: str - autore del libro
            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        Metodi:
            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            return_book()- Contrassegna il libro come restituito.

    Classe Member:
        Attributi:
            member_id: str - identificativo del membro.
            name: str - il nome del membro.
            borrowed_books: list[Book] - lista dei libri presi in prestito.
        Metodi:
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.

    Classe Library:
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Metodi:
            
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.

'''

class Book:

    book_id: str 
    title: str 
    author: str
    is_borrowed: bool

    def __init__(self, book_id:str, title:str, author:str) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self) -> None:
        if self.is_borrowed:
            raise ValueError('Book is already borrowed')
        self.is_borrowed = True

    def return_book(self) -> None:
        if not self.is_borrowed:
            raise ValueError('libro no è stato prestato')
        self.is_borrowed = False

class Member:

    member_id: str
    name: str
    borrowed_books: list[Book]

    def __init__(self, member_id: str, name:str, borrowed_book:list[Book] = None) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_book or []

    def borrow_book(self, book:Book) -> None:
        if book in self.borrowed_books:
            raise ValueError('il libro gia presente')
        self.borrowed_books.append(book)
        book.borrow()

    def return_book(self, book:Book) -> None:
        if book not in self.borrowed_books:
            raise ValueError('Book not borrowed by this member')
        self.borrowed_books.remove(book)
        book.return_book()

    def get_borrowed_books(self) -> list[Book]:
        return self.borrowed_books


class Library:

    books: dict[str, Book]
    members: dict[str, Member]

    def __init__(self, books:dict[str,Book] = None, members:dict[str,Member] = None) -> None:
        self.books = books or {}
        self.members = members or {}

    def add_book(self, book_id:str, title:str, author:str) -> None:
        if book_id in self.books:
            raise KeyError('il libro gia presente')
        self.books[book_id] = Book(book_id, title, author)

    def register_member(self, member_id:str, name:str) -> None:
        if member_id in self.members:
            raise KeyError('utente è gia registrato')
        self.members[member_id] = Member(member_id, name)

    def borrow_book(self, member_id:str, book_id:str) -> None:
        if member_id not in self.members: 
            raise ValueError('Member not found')
        if book_id not in self.books:
            raise ValueError('Book not found')
        self.members[member_id].borrow_book(self.books[book_id])

    def return_book(self, member_id:str, book_id:str) -> None:
        if member_id not in self.members or book_id not in self.books:
            raise KeyError('utente o libro non presenti')
        self.members[member_id].return_book(self.books[book_id])
    
    def get_borrowed_books(self, member_id:str) -> list[Book]:
        list_books:list[Book] = self.members[member_id].get_borrowed_books()
        list_titles:list[str] = []
        for book in list_books:
            list_titles.append(book.title)
        return list_titles

        

if __name__ == "__main__":

    # library = Library()

    # library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
    # library.add_book("B002", "1984", "George Orwell")
    # library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

    # # Register members
    # library.register_member("M001", "Alice")
    # library.register_member("M002", "Bob")
    # library.register_member("M003", "Charlie")

    # # Borrow books
    # library.borrow_book("M001", "B001")
    # library.borrow_book("M002", "B002")

    # print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
    # print(library.get_borrowed_books("M002"))  # Expected output: ['1984']

 	

    library = Library()

    library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("B002", "1984", "George Orwell")
    library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

    # Register members
    library.register_member("M001", "Alice")
    library.register_member("M002", "Bob")
    library.register_member("M003", "Charlie")

    # Borrow books
    library.borrow_book("M001", "B001")
    library.borrow_book("M002", "B002")

    library.return_book("M001", "B001")
    library.return_book("M002", "B002")

    # Check borrowed books after returning
    print(library.get_borrowed_books("M001"))
    print(library.get_borrowed_books("M002"))