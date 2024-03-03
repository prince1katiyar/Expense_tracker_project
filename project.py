class Library:
    pass

    def __init__(self,books):
        self.books = books



    def show_avail_books(self):
        print("you can get these books from the library")
        print("+++++++++++++++++++++++++++++++++++++++++")
        for book ,borrower in self.books.items():
            if borrower == "Free":
                print(book)

    def lend_book(self, requested_book, name):
        if self.books[requested_book] == 'Free':
            print(
                f'{requested_book} has been marked'
                f' as \'Borrowed\' by: {name}')
            self.books[requested_book] = name
            return True
        
        else:
            print(
                        
               f'Sorry, the {requested_book} is currently'
               f'not avaible : {self.books[requested_book]}'
               )
            return False
            

       



    def return_book(self,returended_book):
        self.books[returended_book]="Free"
        print("fine thank you for returning the book")

        
 





class student:


    def __init__(self,name ,library):
        self.name = name
        self.library = library
        self.books = []
    

    def view_borrowed(self):
        if not self.books:
            print("you have't borrowed any books")
        else:
            for book in self.books:
                print(book)

    
    def request_book(self):
        book = input(
            'Enter the name of the book you\'d like to borrow >>::  ')

        if self.library.lend_book(book,self.name):
            self.books.append(book)


        


    def return_book(self):
        book =input(
            'Enter the name of the book you\'d like to return >>::  ')

        if book in self.books:
            self.library.return_book(book)
        else:
            print('You haven\'t borrowed that book, try another...')







def create_mylib():

    books = {
        "python coding": "Free",
        "data science": "Free",
        "machine learning": "Free" 
    }


    library=Library(books)

    student_example =student("your name",library)


    while True: 
        print("""
              *********** Books in Library ***********
              
              1.Display Available Books
              2.Borrow a Book
              3.Return a Book
              4.View Your Books
              5.Exit 
               """)
        

        choice = int(input("enter your choice"))

        if choice == 1:
            print()
            library.show_avail_books()

        elif choice == 2:
            print()
            student_example.request_book()

        elif choice ==3:
            print()
            student_example.return_book()

        elif choice ==4:
            print()
            student_example.view_borrowed()

        elif choice ==5:
            print("now thank you your project is ready , thank you using hte library")
            exit()




create_mylib()
