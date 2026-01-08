class Vehicle:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):  # GETTER
        return self.__brand

    def set_brand(self, value):  # SETTER
        self.__brand = value

    def get_model(self):  # GETTER
        return self.__model

    def set_model(self, value):  # SETTER
        self.__model = value

    def display_details(self):
        print(f"Vehicle: {self.__brand} {self.__model}")

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.__seats = seats

    def get_seats(self):  # GETTER
        return self.__seats

    def set_seats(self, value):  # SETTER
        self.__seats = value

    def display_details(self):  # OVERRIDDEN
        print(f"Car: {self.get_brand()} {self.get_model()}, Seats: {self.__seats}")

class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.__capacity = capacity

    def get_capacity(self):  # GETTER
        return self.__capacity

    def set_capacity(self, value):  # SETTER
        self.__capacity = value

    def display_details(self):  # OVERRIDDEN
        print(f"Truck: {self.get_brand()} {self.get_model()}, Capacity: {self.__capacity} tons")

vehicles = [
    Car("Toyota", "Vios", 5),
    Truck("Isuzu", "Elf", 3.5),
    Vehicle("Generic", "ModelX")
]

while True:
    print("\nVEHICLE MANAGEMENT SYSTEM")
    print("1. View All Vehicles")
    print("2. Add New Vehicle")
    print("3. Update Vehicle")
    print("4. Delete Vehicle")
    print("5. Encapsulation Test")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        if not vehicles:
            print("No vehicles found.")
        else:
            for i, v in enumerate(vehicles, start=1):  # TRAVERSAL
                print(f"{i}. ", end="")
                v.display_details()

    elif choice == "2":
        kind = input("Type (Car/Truck/Other): ").strip().lower()
        brand = input("Enter brand: ")
        model = input("Enter model: ")

        # OBJECT CREATION
        if kind == "car":
            seats = int(input("Enter number of seats: "))
            vehicles.append(Car(brand, model, seats))
        elif kind == "truck":
            capacity = float(input("Enter capacity in tons: "))
            vehicles.append(Truck(brand, model, capacity))
        else:
            vehicles.append(Vehicle(brand, model))
        print(f"{brand} {model} added as {kind.title()}.")

    elif choice == "3":
        index = int(input("Enter vehicle number to update: ")) - 1
        if 0 <= index < len(vehicles):
            new_brand = input("Enter new brand: ")
            new_model = input("Enter new model: ")
            vehicles[index].set_brand(new_brand)
            vehicles[index].set_model(new_model)

            if isinstance(vehicles[index], Car):
                new_seats = int(input("Enter new seat count: "))
                vehicles[index].set_seats(new_seats)
            elif isinstance(vehicles[index], Truck):
                new_capacity = float(input("Enter new capacity in tons: "))
                vehicles[index].set_capacity(new_capacity)

            print("Vehicle updated.")
        else:
            print("Invalid selection.")

    elif choice == "4":
        index = int(input("Enter vehicle number to delete: ")) - 1
        if 0 <= index < len(vehicles):
            removed = vehicles.pop(index)
            print(f"{removed.get_brand()} {removed.get_model()} deleted.")
        else:
            print("Invalid selection.")

    elif choice == "5":  # ENCAPSULATION TEST
        for v in vehicles:
            print(f"{v.get_brand()} | Model: {v.get_model()}", end="")
            if isinstance(v, Car):
                print(f" | Seats: {v.get_seats()}")
            elif isinstance(v, Truck):
                print(f" | Capacity: {v.get_capacity()} tons")
            else:
                print()

    elif choice == "6":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")