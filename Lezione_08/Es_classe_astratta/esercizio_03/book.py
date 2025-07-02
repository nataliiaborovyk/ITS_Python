class Book:

    def __init__(self, title:str, author:str, isbn:int):
        self._title = title
        self._author = author
        self._isbn = isbn

    def get_book(self):
        return self._title, self._author, self._isbn

    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author
    
    def get_isbn(self):
        return self._isbn
    
    def __str__(self):
        return f"Titolo: {self._title}, Autore: {self._author}, Isbn: {self._isbn}"
    
    @classmethod
    def from_string(cls, book_str:str):
        words: list[str] = book_str.split(',')
        return Book(words[0], words[1], words[2])
    

