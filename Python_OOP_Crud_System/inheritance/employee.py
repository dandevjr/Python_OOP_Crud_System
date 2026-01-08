class Employee:
    def __init__(self, name, position):
        self.__name = name
        self.__position = position

    def get_name(self):  # GETTER
        return self.__name

    def set_name(self, value):  # SETTER
        self.__name = value

    def get_position(self):  # GETTER
        return self.__position

    def set_position(self, value):  # SETTER
        self.__position = value

    def display_details(self):
        print(f"Employee: {self.__name}, Position: {self.__position}")

class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.__department = department

    def get_department(self):  # GETTER
        return self.__department

    def set_department(self, value):  # SETTER
        self.__department = value

    def display_details(self):  # OVERRIDDEN
        super().display_details()  # CALLING PARENT METHOD
        print(f"Department: {self.__department}")

class Director(Manager):
    def __init__(self, name, position, department, region):
        super().__init__(name, position, department)
        self.__region = region

    def get_region(self):  # GETTER
        return self.__region

    def set_region(self, value):  # SETTER
        self.__region = value

    def display_details(self):  # OVERRIDDEN
        super().display_details()  # CALLING PARENT METHOD
        print(f"Region: {self.__region}")

staff = [
    Employee("Alice", "Developer"),
    Manager("Bob", "Team Lead", "IT"),
    Director("Carol", "Director", "Operations", "Visayas")
]

while True:
    print("\nSTAFF HIERARCHY SYSTEM")
    print("1. View All Staff")
    print("2. Add New Staff")
    print("3. Update Staff")
    print("4. Delete Staff")
    print("5. Encapsulation Test")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        if not staff:
            print("No staff records found.")
        else:
            for i, s in enumerate(staff, start=1):  # TRAVERSAL
                print(f"{i}. ", end="")
                s.display_details()

    elif choice == "2":
        role = input("Role (Employee/Manager/Director): ").strip().lower()
        name = input("Enter name: ")
        position = input("Enter position: ")

        # OBJECT CREATION
        if role == "manager":
            dept = input("Enter department: ")
            staff.append(Manager(name, position, dept))
        elif role == "director":
            dept = input("Enter department: ")
            region = input("Enter region: ")
            staff.append(Director(name, position, dept, region))
        else:
            staff.append(Employee(name, position))
        print(f"{name} added as {role.title()}.")

    elif choice == "3":
        index = int(input("Enter staff number to update: ")) - 1
        if 0 <= index < len(staff):
            new_name = input("Enter new name: ")
            new_position = input("Enter new position: ")
            staff[index].set_name(new_name)
            staff[index].set_position(new_position)

            if isinstance(staff[index], Manager):
                new_dept = input("Enter new department: ")
                staff[index].set_department(new_dept)
            if isinstance(staff[index], Director):
                new_region = input("Enter new region: ")
                staff[index].set_region(new_region)

            print("Staff updated.")
        else:
            print("Invalid selection.")

    elif choice == "4":
        index = int(input("Enter staff number to delete: ")) - 1
        if 0 <= index < len(staff):
            removed = staff.pop(index)
            print(f"{removed.get_name()} deleted.")
        else:
            print("Invalid selection.")

    elif choice == "5":  # ENCAPSULATION TEST
        for s in staff:
            print(f"{s.get_name()} | Position: {s.get_position()}", end="")
            if isinstance(s, Manager):
                print(f" | Department: {s.get_department()}", end="")
            if isinstance(s, Director):
                print(f" | Region: {s.get_region()}", end="")
            print()

    elif choice == "6":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")