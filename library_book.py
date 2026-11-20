
class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        Book.total_books += 1

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed.")

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"


# Create book objects
book1 = Book("The Fault in Our Stars", "John Green")
book2 = Book("El Filibusterismo", "Jose Rizal")

# Test borrowing and returning
book1.borrow()
book1.borrow()
book1.return_book()

# Display book information
print(book1)
print(repr(book2))

# Display total number of books
print("Total books:", Book.total_books)