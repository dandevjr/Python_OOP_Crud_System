class Person:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address

    def __del__(self):
        print(f"Person '{self.__name}' has been deleted.")

    def get_name(self):  # GETTER
        return self.__name

    def set_name(self, value):  # SETTER
        self.__name = value

    def get_age(self):  # GETTER
        return self.__age

    def set_age(self, value):  # SETTER
        self.__age = value

    def get_address(self):  # GETTER
        return self.__address

    def set_address(self, value):  # SETTER
        self.__address = value

    def display_details(self):
        print(f"Name: {self.__name}, Age: {self.__age}, Address: {self.__address}")

people = [
    Person("Jack", 25, "Tacloban City"),
    Person("Romar", 30, "Ormoc City")
]

while True:
    print("\nPERSON INFORMATION SYSTEM")
    print("1. View All Persons")
    print("2. Add New Person")
    print("3. Update Person")
    print("4. Delete Person")
    print("5. Encapsulation Test")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        if not people:
            print("No person records found.")
        else:
            for i, p in enumerate(people, start=1):  # TRAVERSAL
                print(f"{i}. ", end="")
                p.display_details()

    elif choice == "2":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        address = input("Enter address: ")
        people.append(Person(name, age, address))  # OBJECT CREATION
        print(f"'{name}' added successfully.")

    elif choice == "3":
        update_name = input("Enter name of person to update: ")
        found = False
        for p in people:
            if p.get_name().lower() == update_name.lower():
                new_age = int(input("Enter new age: "))
                new_address = input("Enter new address: ")
                p.set_age(new_age)
                p.set_address(new_address)
                print("Person updated.")
                found = True
                break
        if not found:
            print("Person not found.")

    elif choice == "4":
        delete_name = input("Enter name of person to delete: ")
        for p in people:
            if p.get_name().lower() == delete_name.lower():
                people.remove(p)
                del p
                break
        else:
            print("Person not found.")

    elif choice == "5":  # ENCAPSULATION TEST
        for p in people:
            print(f"{p.get_name()} | Age: {p.get_age()} | Address: {p.get_address()}")

    elif choice == "6":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")