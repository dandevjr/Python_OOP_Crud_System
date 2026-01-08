class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):  # GETTER
        return self.__name

    def set_name(self, value):  # SETTER
        self.__name = value

    def get_salary(self):  # GETTER
        return self.__salary

    def set_salary(self, value):  # SETTER
        if value >= 0:
            self.__salary = value
        else:
            print("Invalid salary. Must be non-negative.")

    def display_details(self):
        print(f"Name: {self.__name}, Salary: {self.__salary:.2f}")

employees = [
    Employee("Jack", 25000),
    Employee("Romar", 30000)
]

while True:
    print("\nEMPLOYEE MANAGEMENT SYSTEM")
    print("1. View All Employees")
    print("2. Add New Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Encapsulation Test")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        if not employees:
            print("No employee records found.")
        else:
            for i, e in enumerate(employees, start=1):  # TRAVERSAL
                print(f"{i}. ", end="")
                e.display_details()

    elif choice == "2":
        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))
        if salary < 0:
            print("Error: Salary must be non-negative.")
        else:
            employees.append(Employee(name, salary))  # OBJECT CREATION
            print(f"'{name}' added successfully.")

    elif choice == "3":
        update_name = input("Enter name of employee to update: ")
        found = False
        for e in employees:
            if e.get_name().lower() == update_name.lower():
                new_name = input("Enter new name: ")
                new_salary = float(input("Enter new salary: "))
                e.set_name(new_name)
                e.set_salary(new_salary)
                print("Employee updated.")
                found = True
                break
        if not found:
            print("Employee not found.")

    elif choice == "4":
        delete_name = input("Enter name of employee to delete: ")
        for e in employees:
            if e.get_name().lower() == delete_name.lower():
                employees.remove(e)
                print(f"Employee '{delete_name}' deleted.")
                break
        else:
            print("Employee not found.")

    elif choice == "5":  # ENCAPSULATION TEST
        for e in employees:
            print(f"{e.get_name()} | Salary: {e.get_salary():.2f}")

    elif choice == "6":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")