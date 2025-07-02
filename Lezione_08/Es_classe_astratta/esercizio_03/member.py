from book import Book

class Member:

    def __init__(self, name:str, member_id:int, borrowed_books:list = None):
        self._name = name
        self._member_id = member_id
        if borrowed_books is None:
            self._borrowed_books = []
        else:
            self._borrowed_books = borrowed_books

    def get_name(self):
        return self._name
    
    def get_id(self):
        return self._member_id

    def borrow_book(self, b:Book):
        if b not in self._borrowed_books:
            self._borrowed_books.append(b)
        else:
            print(f"{b.get_title()} hai gia prestato")

    def return_book(self, b:Book):
        if b in self._borrowed_books:
            self._borrowed_books.remove(b)
        else:
            print(f"{b.get_title()} non hai prestato")

    def __str__(self):
        result: str = f"Nome: {self._name}, Member id: {self._member_id}, Libri prestati: "
        for i in self._borrowed_books:
            result += f"\n  Titolo: {i.get_title()}, Autore: {i.get_author()}, Isbn: {i.get_isbn()}"
        return result

    @classmethod
    def from_string(cls, members_info:str):
        words: list[str] = members_info.split(",")
        return Member(words[0], words[1])
    


    