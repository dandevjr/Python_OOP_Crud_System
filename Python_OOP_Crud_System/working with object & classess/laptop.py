class Laptop:
    def __init__(self, brand, model, specs):
        self.__brand = brand
        self.__model = model
        self.__specs = specs
        self.__power = False

    def get_brand(self):  # GETTER
        return self.__brand

    def set_brand(self, value):  # SETTER
        self.__brand = value

    def get_model(self):  # GETTER
        return self.__model

    def set_model(self, value):  # SETTER
        self.__model = value

    def get_specs(self):  # GETTER
        return self.__specs

    def set_specs(self, value):  # SETTER
        self.__specs = value

    def turn_on(self):
        if not self.__power:
            self.__power = True
            print(f"{self.__brand} {self.__model} is now ON.")
        else:
            print("Laptop is already ON.")

    def turn_off(self):
        if self.__power:
            self.__power = False
            print(f"{self.__brand} {self.__model} is now OFF.")
        else:
            print("Laptop is already OFF.")

    def display_details(self):
        status = "ON" if self.__power else "OFF"
        print(f"Brand: {self.__brand}, Model: {self.__model}, Specs: {self.__specs}, Power: {status}")

laptops = [
    Laptop("Dell", "XPS 13", "Intel i7, 16GB RAM, 512GB SSD"),
    Laptop("HP", "Pavilion", "AMD Ryzen 5, 8GB RAM, 256GB SSD")
]

while True:
    print("\nLAPTOP SYSTEM")
    print("1. View All Laptops")
    print("2. Add New Laptop")
    print("3. Update Laptop")
    print("4. Turn On / Off Laptop")
    print("5. Delete Laptop")
    print("6. Encapsulation Test")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "1":
        if not laptops:
            print("No laptop records found.")
        else:
            for i, l in enumerate(laptops, start=1):  # TRAVERSAL
                print(f"{i}. ", end="")
                l.display_details()

    elif choice == "2":
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        specs = input("Enter specs: ")
        laptops.append(Laptop(brand, model, specs))  # OBJECT CREATION
        print(f"'{brand} {model}' added successfully.")

    elif choice == "3":
        update_model = input("Enter model of laptop to update: ")
        found = False
        for l in laptops:
            if l.get_model().lower() == update_model.lower():
                new_brand = input("Enter new brand: ")
                new_specs = input("Enter new specs: ")
                l.set_brand(new_brand)
                l.set_specs(new_specs)
                print("Laptop updated.")
                found = True
                break
        if not found:
            print("Laptop not found.")

    elif choice == "4":
        model = input("Enter model of laptop to control: ")
        for l in laptops:
            if l.get_model().lower() == model.lower():
                action = input("Turn ON or OFF (O/F): ").strip().upper()
                if action == "O":
                    l.turn_on()
                elif action == "F":
                    l.turn_off()
                else:
                    print("Invalid action.")
                break
        else:
            print("Laptop not found.")

    elif choice == "5":
        delete_model = input("Enter model of laptop to delete: ")
        for l in laptops:
            if l.get_model().lower() == delete_model.lower():
                laptops.remove(l)
                print(f"Laptop '{delete_model}' deleted.")
                break
        else:
            print("Laptop not found.")

    elif choice == "6":  # ENCAPSULATION TEST
        for l in laptops:
            print(f"{l.get_brand()} | Model: {l.get_model()} | Specs: {l.get_specs()}")

    elif choice == "7":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")