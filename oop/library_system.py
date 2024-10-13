# Base Class - Book
class Book:
    """A base class to represent a generic book."""
    def __init__(self, title, author):
        """Initialize the book's title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


# Derived Class - EBook
class EBook(Book):
    """A class to represent an e-book, inheriting from Book."""
    def __init__(self, title, author, file_size):
        """Initialize the e-book with title, author, and file size."""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the e-book."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class - PrintBook
class PrintBook(Book):
    """A class to represent a print book, inheriting from Book."""
    def __init__(self, title, author, page_count):
        """Initialize the print book with title, author, and page count."""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Library Class - Demonstrating Composition
class Library:
    """A class to represent a library that manages a collection of books."""
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)
