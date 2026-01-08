class Operation:
    def __init__(self, number1, number2):
        self.__number1 = number1
        self.__number2 = number2

    def get_number1(self):  # GETTER
        return self.__number1

    def set_number1(self, value):  # SETTER
        self.__number1 = value

    def get_number2(self):  # GETTER
        return self.__number2

    def set_number2(self, value):  # SETTER
        self.__number2 = value

    def add(self):
        return self.__number1 + self.__number2

    def subtract(self):
        return self.__number1 - self.__number2

    def multiply(self):
        return self.__number1 * self.__number2

    def divide(self):
        if self.__number2 != 0:
            return self.__number1 / self.__number2
        else:
            return "Undefined"

    def display_details(self):
        print(f"Num1: {self.__number1}, Num2: {self.__number2}, Add: {self.add()}, Subtract: {self.subtract()}, Multiply: {self.multiply()}, Divide: {self.divide()}")

operations = [
    Operation(10, 5),
    Operation(20, 4)
]

procedural_data = [
    (8, 2),
    (15, 3)
]

def procedural_add(a, b):
    return a + b

def procedural_subtract(a, b):
    return a - b

def procedural_multiply(a, b):
    return a * b

def procedural_divide(a, b):
    return a / b if b != 0 else "Undefined"

while True:
    print("\nPROGRAMMING STYLE DEMO")
    print("1. View OOP Operations")
    print("2. Add OOP Operation")
    print("3. Update OOP Operation")
    print("4. Delete OOP Operation")
    print("5. Encapsulation Test")
    print("6. View Procedural Operations")
    print("7. Add Procedural Operation")
    print("8. Exit")

    choice = input("Choose an option (1-8): ")

    if choice == "1":
        if not operations:
            print("No OOP operations found.")
        else:
            for i, op in enumerate(operations, start=1):  # TRAVERSAL
                print(f"{i}. ", end="")
                op.display_details()

    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operations.append(Operation(num1, num2))  # OBJECT CREATION
        print("OOP operation added.")

    elif choice == "3":
        index = int(input("Enter OOP operation number to update: ")) - 1
        if 0 <= index < len(operations):
            new1 = float(input("Enter new first number: "))
            new2 = float(input("Enter new second number: "))
            operations[index].set_number1(new1)
            operations[index].set_number2(new2)
            print("OOP operation updated.")
        else:
            print("Invalid selection.")

    elif choice == "4":
        index = int(input("Enter OOP operation number to delete: ")) - 1
        if 0 <= index < len(operations):
            operations.pop(index)
            print("OOP operation deleted.")
        else:
            print("Invalid selection.")

    elif choice == "5":  # ENCAPSULATION TEST
        for op in operations:
            print(f"Access: Num1={op.get_number1()}, Num2={op.get_number2()}, Add={op.add()}")

    elif choice == "6":
        if not procedural_data:
            print("No procedural operations found.")
        else:
            for i, (a, b) in enumerate(procedural_data, start=1):  # TRAVERSAL
                print(f"{i}. Num1: {a}, Num2: {b}, Add: {procedural_add(a, b)}, Subtract: {procedural_subtract(a, b)}, Multiply: {procedural_multiply(a, b)}, Divide: {procedural_divide(a, b)}")

    elif choice == "7":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        procedural_data.append((a, b))
        print("Procedural operation added.")

    elif choice == "8":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")