from book import Book
from member import Member

class Library:
    total_books:int = 0
     
    def __init__(self, list_books: list[Book] = None, list_members:list[Member] = None) -> None:
        if list_books is None:
            self._list_books = []
        else: 
            self._list_books = list_books
            total_books += 1
        if list_members is None:
            self._list_members = []
        else: 
            self._list_books = list_books
    
    def add_book(self, b:Book):
        if b not in self._list_books:
            self._list_books.append(b)
            Library.total_books += 1
        else:
            print(f"Libro: \nTitolo: {b.get_title()}, Autore: {b.get_author()}, Isbn: {b.get_isbn()} è gia presentre in biblioteca")

    def remove_book(self, b:Book):
        if b in self._list_books:
            self._list_books.remove(b)
        else:
            return f"Libro: \nTitolo: {b.get_title()}, Autore: {b.get_author()}, Isbn: {b.get_isbn()} non è presentre in biblioteca"

    def register_member(self, m:Member):
        if m not in self._list_members:
            self._list_members.append(m)
        else:
            return f"Member: {m.get_name()} con id {m.get_id()}  è gia registrato"
        
    def lend_book(self, b:Book, m:Member):
        if b in self._list_books:
            if m in self._list_members:
                m.borrow_book(b)
            else:
                return f"{m.get_name()} non è registrato "
        else:
            return f"{b.get_title()} di {b.get_author()} non e presente in biblioteca"

    def __str__(self):
        return f"\nlibrary contains: \n   Books: \n{[b.get_book() for b in self._list_books]} \n   Members: \n{[m.get_name() for m in self._list_members]}"

