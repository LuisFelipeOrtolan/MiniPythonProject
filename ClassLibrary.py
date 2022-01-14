
# Class that implements the object Library.
class Library:
    books = [] # Array of Books with all the books in the library.
    # Array of integers with how many books there are avaliable for each one.
    # Obs: books[i] and books_amount[i] should be about the same book.
    books_amount = [] 
    issues = [] # Array of Issues with all the issues in the library.
    name = None # The name of the Library. 

    # Class's constructor.
    # Input: A string with the library's name.
    # Output: A Library object.
    def __init__(self, name):
        self.name = name

    # Function to transform a library in a string.
    # Input: 
    # Output: A string with all library's information.
    def __str__(self):
        string = "Welcome to " + self.name + "\n" # Print the library's name.
        string += "Our current books are: \n\n" # Print all books in library.
        i = 1
        for book in self.books:
            string += "["+str(i)+"]" + " " + str(book) + "Amount: " + str(self.books_amount[i-1]) + "\n\n"
            i += 1
        return string

    # Function that returns all the issues or for a specific id.
    # Input: A positive integer that represents the customer's id. If 0, return all.
    # Output: A list with Issues.
    def get_issues(self, id = 0):
        if id == 0: # If 0, return all issues.
            return self.issues
        else: # Return only issues for that specific user.
            my_issues = []
            for issue in self.issues: # For every issue in the list,
                if issue.person == id: # Check if the issue is for this user.
                    my_issues.append(issue) # If it is, add to the list.
            return my_issues

    # Function that adds a book to the library.
    # Input: A Book and an integer with how many books are avaliable.
    # Output: The book and the amount are added to the lists.
    def add_book(self, book, amount=1):
        if book not in self.books: # If the book was not already on the list,
            self.books.append(book) # Add the Book to the list.
            self.books_amount.append(amount) # Add how many books are avaliable.
        else: # If the book is already on the list, 
            self.books_amount[self.books.index(book)] += amount # Just add the new amount to the current.

    # Function that deletes a book from the library.
    # Input: A Book and a boolean that indicates if all the books must be removed or just one.
    # Output: A book removed from the library. False if the book is not completly removed.
    def delete_book(self, book, all=False):
        if all == True: # If all books must be removed,
            for issue in self.get_issues(): # Search if book is issued.
                if issue.book_issued == book: # If it is, the book can't be removed.
                    print("Book is issued, so you can't delete it.")
                    return False
            # If it was not issued, remove the book and the amount avaliable.
            self.books_amount.pop(self.books.index(book))
            self.books.remove(book)
        else: # If only one book must be removed,
            issued = False # Boolean that indicates if there is a book issued of the same model.
            for issue in self.get_issues(): # Checks if there is a book issued,
                    if issue.book_issued == book: # If it is, mark as True.
                        issued = True
            # If there are more than one of that book is avaliable
            # Or there is only one avaliable, but there are also others that are issued.
            if (self.books_amount[self.books.index(book)] > 1) | ((self.books_amount[self.books.index(book)] == 1) & (issued == True)):
                self.books_amount[self.books.index(book)] -= 1 # So just update the amount.
            else: # If there is only one and is not issued, remove the book completly.
                for issue in self.get_issues(): # Search for issues.
                    if issue.book_issued == book: # If the book is issued, it can't be deleted.
                        print("Book is issued, so you can't delete it.")
                        return False
                # Remove the book and the amount from the lists.
                self.books_amount.pop(self.books.index(book))
                self.books.remove(book)

    # Function that issue a book.
    # Input: A issue.
    # Output: A new issue in the library. Also, False if the Issue already exists.
    def issue_book(self, issue):
        if issue not in self.issues: # If the book was not already issued to that customer,
            if(self.books_amount[self.books.index(issue.book_issued)] >= 1): # Check if it is avaliable.
                self.issues.append(issue) # Insert the issue in the list.
                self.books_amount[self.books.index(issue.book_issued)] -= 1 # Update the amount avaliable.
                print("Book borrowed.")
            else: # If it is not avaliable
                print("Book not avaliable.")
        else: # If the book is already borrowed
            print("Book is already borrowed")
            return False

    # Function that returns a book that was issued.
    # Input: An Issue.
    # Output: True if the book was returned, False otherwise
    def return_book(self, issue):
        if issue in self.issues: # If the Issue exists, 
            self.issues.remove(issue) # Remove the Issue.
            self.books_amount[self.books.index(issue.book_issued)] += 1 # Update the amount avaliable.
            print("Book returned")
            return True
        else: # If the Issue does not exists, return False.
            print("You didn't borrow this book")
            return False

    # Return the ID for a book.
    # Input: A Book
    # Output: An integer.
    def get_id_by_book(self, book):
        id = 1 # Index.
        for curr_book in self.books: # Check every book.
            if book == curr_book: # If it is the book we are looking for,
                return id # Return the id.
            else: # Otherwise, just add 1 to the current id.
                id += 1
