class Book:
    # Class variable to count the total number of books
    total_books = 0
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        # Increment the count whenever a new book instance is created
        Book.total_books += 1
        
        
    @classmethod
    def display_total_books(cls):
        print(f"Total books created: {cls.total_books}")

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

# Create an object of Book class
book = Book("1984", "George Orwell", 328)

# Print the book object using both magic methods
print(str(book))  # Output: '1984' by George Orwell
print(repr(book))  # Output: Book(title='1984', author='George Orwell', pages=328)

# Creating book instances
book1 = Book("1984", "George Okon", 350)
book2 = Book("To chill with a bird", "Bon Cumpo", 423)

# Display the total number of books
Book.display_total_books()
