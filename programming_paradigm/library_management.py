# library_management.py

class Book:
    """Represents a single book with a title, author, and check-out status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f'"{self.title}" by {self.author}'


class Library:
    """Manages a collection of books and provides operations for library users."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                book.check_out()
                return f'You have checked out {book}.'
        return f'Sorry, "{title}" is not available.'

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                book.return_book()
                return f'You have returned {book}.'
        return f'"{title}" is not currently checked out.'

    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]
        if not available:
            return "No books are currently available."
        return "\n".join(str(book) for book in available)
