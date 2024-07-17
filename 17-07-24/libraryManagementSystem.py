# Problem:
# Design a simple library management system with the following requirements:
# A Book class with attributes like title, author, and ISBN.
# A Member class with attributes like name, member ID, and a list of borrowed books.
# A Library class to manage books and members, with methods to add books, register members, lend books, and return books.

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def lend_book(self, book, member):
        if book in self.books:
            member.borrow_book(book)
            self.books.remove(book)
            print(f"{book.title} has been borrowed by {member.name}.")
        else:
            print("Book is not available.")

    def return_book(self, book, member):
        member.return_book(book)
        self.books.append(book)
        print(f"{book.title} has been returned by {member.name}.")


# Example usage:
library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
book2 = Book("1984", "George Orwell", "1234567891")
library.add_book(book1)
library.add_book(book2)

member = Member("Alice", "M001")
library.register_member(member)

library.lend_book(book1, member)
library.return_book(book1, member)
