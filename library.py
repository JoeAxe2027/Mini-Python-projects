def add_book(all_books):
    title = input("Enter the title of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    year = int(input("Enter the year of publication: "))
    author = input("Enter the author of the book: ")

    new_book = {
        "title": title,
        "isbn": isbn,
        "year": year,
        "author": author
    }

    all_books[isbn] = new_book
    print("Book added successfully!\n")


def print_book(book):
    print("Title:", book["title"])
    print("ISBN:", book["isbn"])
    print("Year:", book["year"])
    print("Author:", book["author"])
    print()



def show_books(all_books):
    for book in all_books.values():
        print_book(book)


def delete_book(all_books):
    isbn = input("Enter the ISBN of the book you want to delete: ")
    if isbn in all_books:
        del all_books[isbn]
        print("Book deleted successfully!\n")
    else:
        print("Book with the given ISBN not found!\n")


# Main function to manage the library
def library():
    all_books = {}

    while True:
        print("Choose from the following options:")
        print("1. Add a book")
        print("2. Show all books")
        print("3. Delete a book")
        print("4. Done")

        choice = input("Enter your choice: ")

        if choice == '1':
            if add_book:
                add_book(all_books)
            else:
                print("No books in the library!\n")

        elif choice == '2':
            show_books(all_books)

        elif choice == '3':
            delete_book(all_books)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.\n")


library()
