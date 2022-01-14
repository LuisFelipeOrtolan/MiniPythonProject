import ClassBook

# Class that implements the Issue object
class Issue:
    book_issued = None # The book that was issued.
    person = None # The customer's id responsible for the book.

    # Class's constructor.
    # Input: An object of Book class and an integer greather than 1 to represent the customer.
    # Output: An object of class Issue.
    def __init__(self, book, person):
        self.book_issued = book
        self.person = person

    # Function to transform an issue in a string.
    # Input: 
    # Output: A string with all issues's information.
    def __str__(self):
        return "Book " + self.book_issued.name + " issued to " + str(self.person)

    # Function that compares an object to an issue.
    # Input: An object to be compared.
    # Output: True if the object is equal to the issue, False otherwise.
    def __eq__(self, obj):
        if isinstance(obj, Issue) and obj.book_issued == self.book_issued and obj.person == self.person:
            return True
        return False