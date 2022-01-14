"""
    GUI Library Management
    Author: Luís Felipe Corrêa Ortolan
"""

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from GUI import AddBookWindow, AllIssuesWindow, DeleteBookWindow, IssueBookWindow, ReturnBookWindow, Ui_MainWindow
from ClassBook import *
from ClassLibrary import *
from ClassIssue import *
import sys

# Class that runs the GUI.
class RunGui():

    # Class constructor.
    def __init__(self): 
        self.lib = Library("SuperLibrary") # Creates the library.
        self.start_library() # Adds some books.
        app = QtWidgets.QApplication(sys.argv) # Crete the GUI application.
        self.MainWindow = QtWidgets.QMainWindow() # Create the main window for the GUI.
        self.MainWindow.setWindowIcon(QIcon("images/book.png")) # Add the icon to the program.

        self.ui = Ui_MainWindow() # Gets the Main Window design.
        self.ui.setupUi(self.MainWindow) # Applies it to the program.
        self.MainWindow.setWindowTitle("Super Library - Main Window") # Set the title for the program.

        # Set the functions for each button/
        self.ui.AddBookButton.clicked.connect(self.changeWindowToAddBook)
        self.ui.DeleteBookButton.clicked.connect(self.changeWindowToDeleteBook)
        self.ui.IssueBookButton.clicked.connect(self.changeWindowToBorrowBook)
        self.ui.ReturnBookButton.clicked.connect(self.changeWindowToReturnBook)
        self.ui.ListIssuesButton.clicked.connect(self.changeWindowToAllIssues)

        data = [["Id","Book Name", "Author", "Year", "Quantity"]] # Header for the library's books/

        i = 1
        for book in self.lib.books: # Library's books's data.
            data.append([str(i), book.name, book.author, str(book.year_of_release), str(self.lib.books_amount[i-1])])
            i += 1

        # Create table with all library's book.
        self.model = TableModel(data) 
        self.ui.BooksList.setModel(self.model)
        self.ui.BooksList.setShowGrid(False)
        self.ui.BooksList.horizontalHeader().hide()
        self.ui.BooksList.verticalHeader().hide()

        self.MainWindow.show()
        sys.exit(app.exec_()) # End program.

    # Function that changes from the current window to the Main Window.
    def changeWindowToMain(self):
        self.ui.setupUi(self.MainWindow) # Applies it to the program.
        self.MainWindow.setWindowTitle("Super Library - Main Window") # Set the title for the program.

        # Set the functions for each button/
        self.ui.AddBookButton.clicked.connect(self.changeWindowToAddBook)
        self.ui.DeleteBookButton.clicked.connect(self.changeWindowToDeleteBook)
        self.ui.IssueBookButton.clicked.connect(self.changeWindowToBorrowBook)
        self.ui.ReturnBookButton.clicked.connect(self.changeWindowToReturnBook)
        self.ui.ListIssuesButton.clicked.connect(self.changeWindowToAllIssues)

        data = [["Id","Book Name", "Author", "Year", "Quantity"]] # Header for the library's books/

        i = 1
        for book in self.lib.books: # Library's books's data.
            data.append([str(i), book.name, book.author, str(book.year_of_release), str(self.lib.books_amount[i-1])])
            i += 1

        # Create table with all library's book.
        self.model = TableModel(data) 
        self.ui.BooksList.setModel(self.model)
        self.ui.BooksList.setShowGrid(False)
        self.ui.BooksList.horizontalHeader().hide()
        self.ui.BooksList.verticalHeader().hide()

        self.MainWindow.show()

    # Change current window to Add Book Window.
    def changeWindowToAddBook(self):
        self.addBook = AddBookWindow() # Create Add Book Window.
        self.addBook.setupUi(self.MainWindow) # Set the window.
        self.MainWindow.setWindowTitle("Super Library - Add Book") # Update title.
        # Define actions for buttons.
        self.addBook.Send.clicked.connect(self.processInputAddBook) 
        self.addBook.Return.clicked.connect(self.changeWindowToMain)

    # Change current window to Delete Book Window.
    def changeWindowToDeleteBook(self):
        self.deleteBook = DeleteBookWindow() # Create Delete Book Window.
        self.deleteBook.setupUi(self.MainWindow) # Set the window.
        self.MainWindow.setWindowTitle("Super Library - Delete Book") # Update title.
        # Define actions for buttons.
        self.deleteBook.Send.clicked.connect(self.processInputDeleteBook)
        self.deleteBook.Return.clicked.connect(self.changeWindowToMain)

    # Change current window to Issue Book Window.
    def changeWindowToBorrowBook(self):
        self.borrowBook = IssueBookWindow() # Create Issue Book Window.
        self.borrowBook.setupUi(self.MainWindow) # Set the window.
        self.MainWindow.setWindowTitle("Super Library - Issue Book") # Update title.
        # Define action for buttons.
        self.borrowBook.Send.clicked.connect(self.processInputBorrowBook)
        self.borrowBook.Return.clicked.connect(self.changeWindowToMain)

    # Change current window to Return Book Window.
    def changeWindowToReturnBook(self):
        self.returnBook = ReturnBookWindow() # Create Return Book Window.
        self.returnBook.setupUi(self.MainWindow) # Set the window.
        self.MainWindow.setWindowTitle("Super Library - Return Book") # Update title.
        # Define action for buttons.
        self.returnBook.Send.clicked.connect(self.processInputReturnBook)
        self.returnBook.Return.clicked.connect(self.changeWindowToMain)
        
    # Change current window to All Issues Window.
    def changeWindowToAllIssues(self):
        self.allIssues = AllIssuesWindow() # Create All Issues Window.
        self.allIssues.setupUi(self.MainWindow) # Set the window.
        self.MainWindow.setWindowTitle("Super Library - All Issues") # Update title.
        
        data = [["BookID", "ClientID"]] # Create the header.
        
        for issue in self.lib.get_issues(): # For every issue in the library.
            subdata = []
            subdata.append(self.lib.get_id_by_book(issue.book_issued)) # Get id of book issued.
            subdata.append(issue.person) # Get customer's id.
            data.append(subdata) # Append data.

        # Create table.
        self.model = TableModel(data) 
        self.allIssues.IssuesTable.setModel(self.model)
        self.allIssues.IssuesTable.setShowGrid(False)
        self.allIssues.IssuesTable.horizontalHeader().hide()
        self.allIssues.IssuesTable.verticalHeader().hide()

        # Set buttons
        self.allIssues.GoBack.clicked.connect(self.changeWindowToMain)

    # Function that process the input from the Add Book Window.
    def processInputAddBook(self):
        book_name = self.addBook.BookNameInput.text() # Get book name input
        author = self.addBook.AuthorInput.text() # Get author name input.

        # If every field is empty, just return.
        if (book_name == "") & (author == "") & (self.addBook.YearInput.text() == "") & (self.addBook.QuantityInput.text() == ""):
            self.changeWindowToMain()
            return
        try: # Try to read the year of book.
            year = int(self.addBook.YearInput.text())

            if year < 0: # If year is less than zero, it's invalid.
                self.ErrorMessage("Sorry, the year must be a positive number")
                return
        except ValueError: # If value was not an int.
            self.ErrorMessage("Sorry, the year must be a positive number")
            return
        try: # Try to read the amount avaliable.
            quantity = int(self.addBook.QuantityInput.text())

            if quantity < 1: # If amount is less than one, it's invalid.
                self.ErrorMessage("Sorry, the quantity must be greater than 1")
                return
        except ValueError: # If value was not an int.
            self.ErrorMessage("Sorry, the quantity must be greater than 1")
            return

        # Create book and insert.
        b = Book(book_name, year, author) 
        self.lib.add_book(b, quantity)
        self.changeWindowToMain()
        
    # Function that procces the input from Delete Book Window.
    def processInputDeleteBook(self):
        if (self.deleteBook.textEdit.toPlainText() == ""): # If inputs are empty, return to main window.
            self.changeWindowToMain()
            return

        size = len(self.lib.books) # Get how many books there are in the library.
        try: # Try to read which book is going to be deleted.
            id = int(self.deleteBook.textEdit.toPlainText())  
            if (id > size) | (id < 1): # If the id is greater than the size of library or less than 1, invalid. 
                raise ValueError 
        except ValueError:
            self.ErrorMessage("Sorry, the id must be a number between 1 and " + str(size))
            return
        
        allBooks = False
        if self.deleteBook.AllBooksOption.isChecked(): # Checks if all books must be deleted.
            allBooks = True
        i = 1
        for book in self.lib.books: # For every book on the library,
            if i == id: # If it is the one we are looking for, delete it.
                if self.lib.delete_book(book, allBooks) == False:
                    self.ErrorMessage("There is a book issued that cant be deleted")
                    return
                break
            else: # If it is not, keep looking.
                i += 1

        self.changeWindowToMain() # Go back to main window.

    # Function that proces the input from Borrow Book Window.
    def processInputBorrowBook(self):
        # If all inputs are empty, return to main window.
        if (self.borrowBook.textEdit_2.toPlainText() == "") & (self.borrowBook.textEdit.toPlainText() == ""):
            self.changeWindowToMain()
            return
        
        try: # Try to read the customer's id.
            idUser = int(self.borrowBook.textEdit_2.toPlainText())
        except ValueError: # If input was not an int.
            self.ErrorMessage("Sorry, the user id must be a positive number")
            return

        size = len(self.lib.books) # Get size of the library.
        try: # Try to read the book's id.
            idBook = int(self.borrowBook.textEdit.toPlainText())
            if (idBook > size) | (idBook < 1): # If not beween 1 and size of library, it's unvalid.
                raise ValueError
        except ValueError: # If input was not an int.
            self.ErrorMessage("Sorry, the book id must be a number between 1 and " + str(size))
            return

        bookBorrowed = None # Book that is going to be borrowed.
        i = 1
        for book in self.lib.books: # For every book in the library.
            if i == idBook: # If the book is the one we want.
                bookBorrowed = book
                break
            else:
                i += 1
        issue = Issue(bookBorrowed, idUser) # Create the issue.
        if self.lib.issue_book(issue) == False: # If this customer already borrowd this book.
            self.ErrorMessage("Sorry, this book was already issued for this user.")
            return

        self.changeWindowToMain() # Go back to the main menu.

    # Function that process the input from the Return Book Window.
    def processInputReturnBook(self):
        # If all the inputs are empty, go back to Main Window.
        if (self.returnBook.textEdit_2.toPlainText() == "") & (self.returnBook.textEdit.toPlainText() == ""):
            self.changeWindowToMain()
            return
        
        try: # Try to read the customer's id.
            idUser = int(self.returnBook.textEdit_2.toPlainText())
        except ValueError: # If the input value was not an int.
            self.ErrorMessage("Sorry, the user id must be a positive number")
            return

        size = len(self.lib.books) # Get the size of the library.
        try: # Try to read the book's id.
            idBook = int(self.returnBook.textEdit.toPlainText())
            if (idBook > size) | (idBook < 0): # If book id is not valid.
                raise ValueError
        except ValueError: # If input was not an int.
            self.ErrorMessage("Sorry, the book id must be a number between 1 and " + str(size))
            return

        bookBorrowed = None # The book is being borrowed.
        i = 1
        for book in self.lib.books: # For every book in the library.
            if i == idBook: # If it is the one we are looking for.
                bookBorrowed = book
                break
            else: # If it is not the one we are looking for, continue the search.
                i += 1
        issue = Issue(bookBorrowed, idUser) # Create the issue.
        if self.lib.return_book(issue) == False: # If the customer has not borrowed this book.
            self.ErrorMessage("Sorry, this book was not issued to this customer")
            return
            
        self.changeWindowToMain()

    # Function that insert two initial books to the library.
    def start_library(self):
        book = Book("Harry Potter", 1978, "Jen")
        self.lib.add_book(book)
        book = Book("The Hunger Games", 2003, "Rena")
        self.lib.add_book(book)

    # Function that generates the Error Window.
    # Input: A string with the message that is going to be displayed.
    def ErrorMessage(self, message):
        from PyQt5.QtWidgets import QMessageBox

        msg = QMessageBox() # Create the Error Window
        msg.setIcon(QMessageBox.Critical) # Set the icon in the window.
        msg.setText("Error") 
        msg.setInformativeText(message) # Set the input message.
        msg.setWindowTitle("Error") # Set the window title.
        msg.setWindowIcon(QIcon("images/book.png")) # Add the icon to the program.
        msg.exec_() # Show Window.

# Class that implements QAbstractTableModel. 
# It displays the Tables in the program.
class TableModel(QtCore.QAbstractTableModel):
    # Class's constructor.
    def __init__(self, data):
        super(TableModel, self).__init__() # Start the super class.
        self._data = data # Set the data for the table.

    def data(self, index, role): # Get the data from the table.
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index): # Return the number of rows in the table.
        return len(self._data)

    def columnCount(self, index): # Return the number of columns in the table.
        return len(self._data[0])

if __name__ == "__main__":
    RunGui()