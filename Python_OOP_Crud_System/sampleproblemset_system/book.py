class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def get_title(self):  # GETTER
        return self.__title

    def set_title(self, value):  # SETTER
        self.__title = value

    def get_author(self):  # GETTER
        return self.__author

    def set_author(self, value):  # SETTER
        self.__author = value

    def get_isbn(self):  # GETTER
        return self.__isbn

    def set_isbn(self, value):  # SETTER
        self.__isbn = value

    def display_details(self):
        print(f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}")

books = [
    Book("Python Basics", "Jack Coder", "1234567890"),
    Book("OOP Concepts", "Romar Dev", "0987654321")
]

while True:
    print("\nBOOK INFORMATION SYSTEM")
    print("1. View All Books")
    print("2. Add New Book")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Encapsulation Test")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        if not books:
            print("No book records found.")
        else:
            for i, b in enumerate(books, start=1):  # TRAVERSAL
                print(f"{i}. ", end="")
                b.display_details()

    elif choice == "2":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        books.append(Book(title, author, isbn))  # OBJECT CREATION
        print(f"'{title}' added successfully.")

    elif choice == "3":
        update_isbn = input("Enter ISBN of book to update: ")
        found = False
        for b in books:
            if b.get_isbn() == update_isbn:
                new_title = input("Enter new title: ")
                new_author = input("Enter new author: ")
                b.set_title(new_title)
                b.set_author(new_author)
                print("Book updated.")
                found = True
                break
        if not found:
            print("Book with that ISBN not found.")

    elif choice == "4":
        delete_isbn = input("Enter ISBN of book to delete: ")
        for b in books:
            if b.get_isbn() == delete_isbn:
                books.remove(b)
                print(f"Book with ISBN '{delete_isbn}' deleted.")
                break
        else:
            print("Book with that ISBN not found.")

    elif choice == "5":  # ENCAPSULATION TEST
        for b in books:
            print(f"{b.get_title()} by {b.get_author()} | ISBN: {b.get_isbn()}")

    elif choice == "6":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")