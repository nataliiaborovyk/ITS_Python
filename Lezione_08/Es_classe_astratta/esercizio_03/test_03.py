from book import Book
from member import Member
from library import Library

b:Book = Book("Anna", "Marco Rossi", 7673664)
print(b)

book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
divina_commedia:Book = Book.from_string(book_str)
print(divina_commedia)

m1:Member = Member("Carlo", 223344)
m1.borrow_book(b)
m1.borrow_book(divina_commedia)
print(m1)

m1.return_book(b)
print(m1)

member_info: str = "Alex,777888"
m2:Member = Member.from_string(member_info)
print(m2)

lib1:Library = Library()
lib1.add_book(divina_commedia)
lib1.register_member(m1)

print(lib1)