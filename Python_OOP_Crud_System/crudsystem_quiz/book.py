class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__borrowed = 0
        self.copies = copies

    def borrow(self):
        if self.__borrowed < self.copies:
            self.__borrowed += 1
        else:
            print("No copies available.")

    def return_book(self):
        if self.__borrowed > 0:
            self.__borrowed -= 1
        else:
            print("No borrowed copies to return.")

    def get_borrowed(self):  # GETTER
        return self.__borrowed

    def set_borrowed(self, value):  # SETTER
        print("Direct modification of borrowed count not allowed.")

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Borrowed: {self.__borrowed}/{self.copies}")

books = [
    Book("Python Basics", "Jack Coder", "1234567890", 3),
    Book("OOP Concepts", "Romar Dev", "0987654321", 2)
]

while True:
    print("\nLIBRARY BOOK TRACKER")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Encapsulation Test")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        copies = int(input("Enter number of copies: "))
        if copies < 1:
            print("Error: Must have at least one copy.")
        else:
            books.append(Book(title, author, isbn, copies))
            print(f"'{title}' added.")

    elif choice == "2":
        if not books:
            print("No books found.")
        else:
            for i, b in enumerate(books, start=1):
                print(f"{i}. ", end="")
                b.display_details()

    elif choice == "3":
        title = input("Enter book title to borrow: ")
        for b in books:
            if b.title.lower() == title.lower():
                b.borrow()
                break
        else:
            print("Book not found.")

    elif choice == "4":
        title = input("Enter book title to return: ")
        for b in books:
            if b.title.lower() == title.lower():
                b.return_book()
                break
        else:
            print("Book not found.")

    elif choice == "5":  # ENCAPSULATION TEST
        for b in books:
            print(f"{b.title} borrowed access: {b.get_borrowed()}")

    elif choice == "6":
        break

    else:
        print("Invalid choice.")