class Library:
    
    def __init__(self, books):
        self.books = books 

    def show_available_books(self):
        print("These books are available in the library")
        print("+++++++++++===============+++++++++++")
        for book, borrower in self.books.items():
            if borrower == "free":
                print(book)

    def lend_book(self, requested_book, borrower_name):
        if requested_book in self.books:  
            if self.books[requested_book] == "free":
                print(
                    f'{requested_book} has been marked as \'Borrowed\' by: {borrower_name}')
                self.books[requested_book] = borrower_name
                return True 
            else:
                print(
                    f'Sorry, {requested_book} is currently on loan to: {self.books[requested_book]}')
                return False
        else:
            print(f'Sorry, {requested_book} is not available in the library')
            return False

    def return_book(self, returned_book):
        if returned_book in self.books and self.books[returned_book] != "free":
            print(f'Thanks for returning {returned_book}')
            self.books[returned_book] = "free"
        else:
            print(f'Error: {returned_book} is not a valid book or is not borrowed')

class Student:
    
    def __init__(self, name, library):
        self.name = name 
        self.library = library
        self.books = []

    def request_book(self, book_name):
        if self.library.lend_book(book_name, self.name):
            self.books.append(book_name)

    def return_book(self, book_name):
        if book_name in self.books:
            self.library.return_book(book_name)
            self.books.remove(book_name)
        else:
            print(f'Error: {book_name} is not borrowed by {self.name}')

    def view_borrowed(self):
        if not self.books:
            print("You haven't borrowed any books")
        else:
            print("Books you have borrowed:")
            for book in self.books:
                print(book)

def create_lib():
    books = {
        "python coding": "free",
        "data science": "free",
        "machine learning": "free" 
    }

    library1 = Library(books)
    student1 = Student("Your Name", library=library1)

    while True:
        print("""
              *********** Books in Library ***********
            1. Available books
            2. Borrow books 
            3. Return books
            4. View your borrowed books
            5. Exit
        """)

        choice = int(input("Select your choice: "))

        if choice == 1:
            print()
            library1.show_available_books()
        elif choice == 2:
            print()
            book_name = input("Enter the name of the book you want to borrow: ")
            student1.request_book(book_name)
        elif choice == 3:
            print()
            book_name = input("Enter the name of the book you want to return: ")
            student1.return_book(book_name)
        elif choice == 4:
            print()
            student1.view_borrowed()
        elif choice == 5:
            print("Thank you for using the library")
            exit()

create_lib()
