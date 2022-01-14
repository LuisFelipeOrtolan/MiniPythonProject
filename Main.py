"""
    Command Line Library Management
    Author: Luís Felipe Corrêa Ortolan
"""

from ClassBook import *
from ClassIssue import *
from ClassLibrary import *
from ClassUtils import Utils
import time

# Main Class of the program.
class Main(): 
    # Main function.
    def run(self):
        lib = self.start_library("Super Library") # Start object library.
        try: # To avoid KeyBoardInterrupt error message.
            while True: # Main Menu runs unil KeyBoardInterrupt.
                Utils.clear() # Clears console.
                type_user = input("Are you an user or an admin?\n") # Input type of user.
                time.sleep(1) # Wait for a second and clear console.
                Utils.clear()
                if type_user == "admin": # Run admin's menu until option exit.
                    while self.menu_admin(lib) != 0:
                        pass
                else: # If user is not admin, run user's menu.
                    id = None # Set the id as None.
                    while id == None: # While the id was not set,
                        try:  # Try to read an int.
                            id = int(input("What is your id?\n")) # Read an int for the input.
                            Utils.clear() # Clear the console.
                            if id < 1: # If the id is less than one,
                                id = None # Unset the id and raise error.
                                raise ValueError
                        except ValueError: # If the input was not an id.
                            print("Please insert a positive number.")
                            
                    while self.menu_user(lib, id) != 0: # Run user's menu until option exit.
                        pass
        except KeyboardInterrupt:
            print("Goodbye!")
            return

    # Function that starts a library.
    # Input: A string with the library's name.
    # Output: An object Library with two books.
    def start_library(self, name):
        lib = Library(name)
        book = Book("Harry Potter", 1978, "Jen")
        lib.add_book(book)
        book = Book("The Hunger Games", 2003, "Rena")
        lib.add_book(book)
        return lib

    # Function that implements the user's menu.
    # Input: A Library and an integer with the id for the current user.
    def menu_user(self, library, id):
        print(library) # Print current books.
        # Print options.
        print("What do you want to do?")
        print("[1] Borrow a book")
        print("[2] Return a book")
        print("[3] List all my books issued")
        print("[4] Exit")

        option = None
        while option == None: # While option was not set.
            try: # Try to read an option.
                option = int(input()) # Read option
                if (option < 1) | (option > 4): # If option was not avaliable,
                    option = None  # Unset option and raise error.
                    raise ValueError
            except ValueError: # If value was not an int.
                print("Please, insert a number between 1 and 4.")
            except KeyboardInterrupt:
                return 0

        if option == 4: # Exit.
            return 0
        
        if option == 1: # Borrow a book.
            print("Which book do you want to borrow? Insert the id")
            books = library.books # Get all books in the library.
            option = None 
            while option == None: # While option is not set.
                try: # Try to read the option.
                    option = int(input()) # read the option.
                    if (option < 1) | (option > len(books)): # If there is no book to that option,
                        option = None # Unset option and raise error.
                        raise ValueError
                except ValueError: # If value was not an int.
                    print("Please, insert a number between 1 and", str(len(books)) + ".")
                except KeyboardInterrupt:
                    return 0

            book = books[option-1] # Get book that is going to be issued.
            issue = Issue(book, id) # Create issue.
            library.issue_book(issue) # Try to issue the book.
            time.sleep(2) # Wait for two seconds and clear the terminal.
            Utils.clear()
            return 1 # Continue

        if option == 2: # Return book.
            print("Which book do you want to return? Insert the id")
            books = library.books # Get all books from the library.

            option = None
            while option == None: # While option is not set.
                try: # Try to read the option.
                    option = int(input()) 
                    if (option < 1) | (option > len(books)): # If option doesn't have a correspondent book,
                        option = None # Unset vaue and raise error.
                        raise ValueError
                except ValueError: # If value was not an int.
                     print("Please, insert a number between 1 and", str(len(books)) + ".")
                except KeyboardInterrupt:
                    return 0

            book = books[option-1] # Get the book.
            issue = Issue(book, id) # Create the issue.
            library.return_book(issue) # Try to return the book.
            time.sleep(2) # Wait for two seconds and clear terminal.
            Utils.clear()
            return 1 # Continue.

        if option == 3: # List Customer's Issues.
            if library.get_issues(id) == []: # If there are no issues yet.
                print("No issues yet!")
            for issue in library.get_issues(id): # Print every issue for that customer.
                print(issue.book_issued)
            input() # Wait for user to want to clear the terminal.
            Utils.clear()
            return 1 # Continue.

    def menu_admin(self, library):
        print(library) # Print all the books in the library.
        # Print options.
        print("What do you want to do?")
        print("[1] Borrow a book")
        print("[2] Return a book")
        print("[3] Add a book")
        print("[4] Delete a book")
        print("[5] List all issues")
        print("[6] Exit")

        option = None
        while option == None: # While options is not set.
            try: # Try to read an option.
                option = int(input())
                if (option < 1) | (option > 6): # If option is not avaliable,
                    option = None # Unset option and raise error.
                    raise ValueError
            except ValueError: # If input was not an int.
                print("Please, insert a number between 1 and 6.")
            except KeyboardInterrupt:
                return 0

        if option == 6: # Exit.
            return 0
        
        if option == 1: # Borrow book.
            print("Which book do you want to borrow? Insert the id.")
            books = library.books # Get all books in the library,
            option = None
            while option == None: # While option is not set.
                try: # Try to read the option.
                    option = int(input()) 
                    if (option < 1) | (option > len(books)): # If there is not a book to that option.
                        option = None # Unset option and raise error.
                        raise ValueError
                except ValueError: # If input was not an int.
                    print("Please, insert a number between 1 and", str(len(books)) + ".")

            print("Who the book is being borrowed to? Insert the id.")
            customer_id = None
            while customer_id == None: # While customer's id was not set.
                try: 
                    customer_id = int(input())
                    if customer_id <= 0: # If id is equal or less than zero, it's invalid.
                        customer_id = None # Unset customer's id and raise error.
                        raise ValueError
                except ValueError: # If input was not int.
                    print("Please insert a postive number.")
                except KeyboardInterrupt:
                    return 0
                
            book = books[option-1] # Get book.
            issue = Issue(book, customer_id) # Create issue.
            library.issue_book(issue) # Try to issue the book.
            time.sleep(2) # Wait two seconds and clear the terminal
            Utils.clear()
            return 1 # Continue.

        if option == 2: # Return book.
            print("Which book do you want to return? Insert the id.")
            books = library.books # Get all books in the library.

            option = None
            while option == None: # While option is not set.
                try: # Try to read the option.
                    option = int(input())
                    if (option < 1) | (option > len(books)): # If there is not a book to that option,
                        option = None # Unset option and raise error.
                        raise ValueError
                except ValueError: # If input was not an integer.
                     print("Please, insert a number between 1 and", str(len(books)) + ".")
                except KeyboardInterrupt:
                    return 0

            print("Who is returning the book? Insert the id.")
            customer_id = None
            while customer_id == None: # While customer's id is not set.
                try: # Try to read the customer's id.
                    customer_id = int(input())
                    if customer_id <= 0: # If id is equal or less than one, is invalid.
                        customer_id = None # Unset id and raise error.
                        raise ValueError
                except ValueError: # If input was not an int.
                    print("Please insert a postive number.")
                except KeyboardInterrupt:
                    return 0

            book = books[option-1] # Get the book.
            issue = Issue(book, customer_id) # Create the issue.
            library.return_book(issue) # Try to return the book.
            time.sleep(2) # Wait for two seconds and clear the terminal.
            Utils.clear()
            return 1 # Continue

        if option == 3: # Add new book.
            try: 
                name = input("What is the book's name?\n")
                year = None
                while year == None: # While year is not set.
                    try: # Try to read it.
                        year = int(input("In which year it was realesed?\n"))
                        if year < 0: # If year is negative, it's unvalid.
                            year = None # Unset year and raise error.
                            raise ValueError
                    except ValueError:
                        print("Please insert a positive number")
                author = input("Who is the author?\n") # Read author.
                amount = None
                while amount == None: # While amount is not set.
                    try: # Try to read the amount.
                        amount = int(input("How many books are avaliable?\n"))
                        if amount <= 0: # If amount is equal or less than zero, it's unvalid.
                            amount = None # Unset amount and raise error.
                            raise ValueError
                    except ValueError: # If input was not an int.
                        print("Please insert a number greater than 1.")
            except KeyboardInterrupt:
                return 0

            b = Book(name, year, author) # Create book.
            library.add_book(b, amount) # Add book to the library.
            time.sleep(2) # Wait for two seconds and clear the terminal.
            Utils.clear()
            return 1 # Continue.

        if option == 4: # Delete book.
            option = None
            while option == None: # While option is not set.
                try: # Try to read the option.
                    option = int(input("Which book do you want to delete? Please insert the id.\n"))
                    size = len(library.books) # Get the size of the library.
                    if (option < 1) | (option > size): # If the option doesn't have a correspondent book,
                        option = None # Unset option and raise error.
                        raise ValueError
                except ValueError: # If value was not an int.
                    print("Please inser a number between 1 and", str(size) + ".")
                except KeyboardInterrupt:
                    return 0

            try: # Try to read if all books are supposed to be deleted.
                delete_option = input("Do you want to delete all books?\n")
            except KeyboardInterrupt:
                return 0

            b = library.books[option-1] # Get the book.
            if delete_option.lower() == "yes": # If all the books are supposed to be deleted.
                library.delete_book(b, True)
            else: # If only one book is going to be deleted.
                library.delete_book(b,False)
            time.sleep(2) # Wait for two seconds and clear the terminal.
            Utils.clear()
            return 1 # Continue.

        if option == 5: # List all issues.
            if library.get_issues() == []: # If issues is empty.
                print("No issues yet.")
            for issue in library.get_issues(): # Print issues that exists.
                print(issue)
            input() # Wait for user to go back to main window.
            Utils.clear() # Clear terminal
            return 1 # Continue

if __name__ == "__main__": # If this is the main program, run it.
    Main().run()