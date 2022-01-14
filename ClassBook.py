
# Class that implements the Book object
class Book:
    name = None # Book's name.
    year_of_release = None # Year that the book was released.
    author = None # Book's author.

    # Class's constructor.
    # Input: The book's name as a string, a positive integer as the year of release and the author as string.
    # Output: A Book object.
    def __init__(self, name, year_of_release, author):
        # Set class variables.
        self.name = name
        self.year_of_release = year_of_release
        self.author = author

    # Function to transform a book in a string.
    # Input: 
    # Output: A string with all book's information.
    def __str__(self):
        return "Book Title: " + self.name + "\nYear of Release: " + str(self.year_of_release) + "\nAuthor: " + self.author + "\n"

    # Function that compares an object to a book.
    # Input: An object to be compared.
    # Output: True if the object is equal to the book, False otherwise.
    def __eq__(self, obj):
        # If it is a Book and the infos are the same it is the same book.
        if isinstance(obj, Book) and (obj.name == self.name) and (obj.author == self.author) and (obj.year_of_release == self.year_of_release):
            return True
        return False