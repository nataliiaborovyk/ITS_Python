'''
             
            Exercise 3: Library Management System 

Create a Book class containing the following attributes: title, author, isbn. The book class must contains the following methods:
    __str__, method to return a string representation of the book.
    from_string, a class method to create a Book instance from a string in the format "title, author, isbn". It means that you must use the class reference cls to create a new object of the Book class using a string.

Example: 
book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
divina_commedia: Book = Book.from_string(book_str)
In this case, divina_commedia should be an instance of the Book class with:
    title = "La Divina Commedia"
    author = "D. Alighieri"
    isbn = "999000666"

Create a Member class with the following attributes: name, member_id, borrowed_books. The member class must contain the following methods:
    borrow_book, to add a book to the borrowed_books list.
    return_book, to remove a book from the borrowed_books list.
    __str__, method to return a string representation of the member.
    from_string, a class method to create a Member instance from a string in the format "name, member_id". It means that you must use the class reference cls to create a new object of the Member class using a string.

Create a Library class with the following attributes: books, members, total_books (i.e., a class attribute to keep track of the total number of Book instances). The library class must contain the following methods:
    add_book, to add a book to the library and increment total_books.
    remove_book, to remove a book from the library and decrement total_books.
    register_member, to add a member to the library.
    lend_book, to lend a book to a member. It should check if the book is available and if the member is registered.
    __str__, method to return a string representation of the library with the list of books and members.
    library_statistics,  a class method to print the total number of books.

Finally, write a simple driver program. After creating a library, you should begin by creating instances of Book and Member. Wherever appropriate, use class methods (such as from_string) to instantiate objects from strings, improving clarity and modularity.
Once your objects are created, simulate some basic library operations:
    Register new members to the library. This could involve adding Member objects to a collection maintained by the library.
    Add books to the library’s collection.
    Lend books to members. This will involve marking a book as borrowed and associating it with a specific member.
    At each significant step, print the state of the library to track how it changes:
       before lending any book,
        after books have been lent.
'''


class Book:

    @classmethod
    def from_string(cls, frase:str):
        title, author, isbn = frase.split(",")
        return cls(title.strip(), author.strip(), isbn.strip())

    def __init__(self, title:str, author:str, isbn:str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"Title: {self.title}  Author: {self.author} isbn: {self.isbn}"
    
    __repr__ = __str__
    
class Member:

    @classmethod
    def from_string(cls, frase:str):
        name, member_id = frase.split(",")
        return cls(name.strip(), member_id.strip())


    def __init__(self, name:str, member_id:str, borrowed_books: list[Book] = None) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books or []

    def borrow_book(self, isbn:str) -> None:
        if isbn in self.borrowed_books:
            raise ValueError('gia preso')
        self.borrowed_books.append(isbn)

    def return_book(self, isbn:str) -> None:
        if isbn not in self.borrowed_books:
            raise ValueError('non hai prestato')
        self.borrowed_books.remove(isbn)

    def __str__(self) -> str:
        return f"Member: {self.name} | ID: {self.member_id} | Books: {self.borrowed_books}"
    
    __repr__ = __str__

class Library:

    total_books:int = 0

    def __init__(self, books:list[Book] = None, members: list[Member] = None) -> None:
        self.books = books or []
        self.members = members or []

    def add_book(self, book: Book) -> None:
        if book in self.books:
            raise ValueError(' gia presente')
        self.books.append(book)
        Library.total_books += 1

    def remove_book(self, book:Book) -> None:
        if book not in self.books:
            raise ValueError(' non presente')
        self.books.remove(book)
        Library.total_books -= 1

    def register_member(self, member:Member) -> None:
        if member in self.members:
            raise ValueError('gia èresente')
        self.members.append(member)

    def lend_book(self, book:Book, member:Member) -> None:
        if book in self.books and member in self.members:
            member.borrow_book(book.isbn)
            self.books.remove(book)

    @classmethod
    def library_statistics(cls) -> list[Book]:
        return f"libri: {cls.total_books}"

    def __str__(self) -> str:
        return f"Books: {self.books} \n Members: {self.members}"
    

if __name__ == "__main__":
    # --- Driver program per testare Library / Book / Member ---

    # 1) Creo una biblioteca vuota
    lib = Library()
    print("== Stato iniziale ==")
    print(Library.library_statistics())  # totale globale libri (classe)
    print(lib)                           # libri disponibili e membri registrati
    print()

    # 2) Creo Book e Member usando i classmethod from_string (chiarezza e modularità)
    b1 = Book.from_string("La Divina Commedia, D. Alighieri, 999000666")
    b2 = Book.from_string("I Promessi Sposi, A. Manzoni, 111222333")
    b3 = Book.from_string("Il Nome della Rosa, U. Eco, 444555666")

    m1 = Member.from_string("Nat, M001")
    m2 = Member.from_string("Chiara, M002")

    # 3) Registro i membri nella biblioteca
    lib.register_member(m1)
    lib.register_member(m2)

    # 4) Aggiungo i libri alla biblioteca
    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)

    print("== Dopo registrazioni e aggiunte ==")
    print(Library.library_statistics())  # totale globale libri
    print(lib)                           # mostra 3 libri disponibili, 2 membri
    print()

    # 5) Stato PRIMA di prestare
    print("== Prima di prestare libri ==")
    print(lib)
    print(f"Prestiti di {m1.name}: {m1.borrowed_books}")
    print(f"Prestiti di {m2.name}: {m2.borrowed_books}")
    print()

    # 6) Presto alcuni libri
    lib.lend_book(b1, m1)  # presta 'La Divina Commedia' a Nat
    lib.lend_book(b2, m2)  # presta 'I Promessi Sposi' a Chiara

    # 7) Stato DOPO i prestiti
    print("== Dopo i prestiti ==")
    print(lib)  # ora dovrebbe rimanere disponibile solo b3
    print(f"Prestiti di {m1.name}: {m1.borrowed_books}")  # contiene ISBN di b1
    print(f"Prestiti di {m2.name}: {m2.borrowed_books}")  # contiene ISBN di b2
    print(Library.library_statistics())  # il totale globale non cambia coi prestiti
