class Employee:
    def __init__(self, name, salary, bonus, deductions):
        self.name = name
        self.__salary = salary
        self.__bonus = bonus
        self.__deductions = deductions

    def get_salary(self):  # GETTER
        return self.__salary

    def set_salary(self, value):  # SETTER
        print("Direct salary modification not allowed.")

    def get_net_pay(self):
        return self.__salary + self.__bonus - self.__deductions

    def display_details(self):
        print(f"Name: {self.name}, Net Pay: {self.get_net_pay():.2f}")

employees = [
    Employee("Jack", 20000, 3000, 1500),
    Employee("Romar", 18000, 2500, 1200)
]

while True:
    print("\nEMPLOYEE PAYROLL SYSTEM")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Encapsulation Test")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter name: ")
        salary = float(input("Enter salary: "))
        bonus = float(input("Enter bonus: "))
        deductions = float(input("Enter deductions: "))
        if salary < 0 or bonus < 0 or deductions < 0:
            print("Error: Values must be non-negative.")
        else:
            employees.append(Employee(name, salary, bonus, deductions))
            print(f"'{name}' added.")

    elif choice == "2":
        if not employees:
            print("No employees found.")
        else:
            for i, e in enumerate(employees, start=1):
                print(f"{i}. ", end="")
                e.display_details()

    elif choice == "3":  # ENCAPSULATION TEST
        for e in employees:
            print(f"{e.name} salary access: {e.get_salary():.2f}")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")