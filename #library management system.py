#library management system 
available_books = ["book1","book2","book3","book4","book5"]
borrowed_books  = []

def display_books():
    """display available books"""
    global available_books
    print(available_books)

def add_books():
    """add a book to library"""
    global available_books
    book_name = input("Enter book name :").strip()
    if book_name in available_books:
        print("Book is already exist")
    else:
        available_books.append(book_name)
        print(f"{book_name} added book to library")
        

def borrow_books():
    global available_books ,borrowed_books
    book_name = input("Enter book name :").strip()
    if book_name in available_books:
        available_books.remove(book_name)
        borrowed_books.append(book_name)
        print(f"{book_name} borrowed book from library")
    else:
        print("Book is not Available")

def return_book():
    global available_books , borrowed_books
    book_name = input("Enter book name :").strip()
    if book_name in borrowed_books:
        borrowed_books.remove(book_name)
        available_books.append(book_name)
        print(f"{book_name} return to library")

    else:
        print("this book was not borrowed")
        

while True:
    print(f"Library".center(22,"="))
    print("1. Available books")
    print("2. Add books")
    print("3. Borrow books")
    print("4. Return books")
    print("5. Exit")

    choice = input("Enter choice :").strip()

    if choice == "1":
        display_books()

    elif choice == "2":
        add_books()

    elif choice == "3":
        borrow_books()

    elif choice == "4":
        return_book()

    elif choice == "5":
        print("thank you for using library")
        break

    else:
        print("choose between 1 - 6 choice")
