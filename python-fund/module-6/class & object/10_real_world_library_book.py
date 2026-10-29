"""Real-world practice: a book keeps its details and borrowing status."""


class LibraryBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"You borrowed '{self.title}'.")
        else:
            print(f"'{self.title}' has already been borrowed.")

    def return_book(self):
        self.is_available = True
        print(f"You returned '{self.title}'.")


book = LibraryBook("The Blue Umbrella", "Ruskin Bond")
print(book.title, "by", book.author)
book.borrow()
book.borrow()  # This time it is already borrowed.
book.return_book()
