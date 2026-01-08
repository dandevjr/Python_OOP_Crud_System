class Car:
    def __init__(self, brand, fuel=0.0, fuel_capacity=50.0, consumption_per_km=0.08):
        
        self.brand = brand
        self.__fuel = float(fuel)
        self.__odometer = 0.0
        self.__fuel_capacity = float(fuel_capacity)
        self.__consumption = float(consumption_per_km)

    def get_fuel(self):
        return round(self.__fuel, 2)

    def get_odometer(self):
        return round(self.__odometer, 2)

  
    def refuel(self, amount):
        if amount <= 0:
            print("Refuel amount must be positive.")
            return
        new_level = min(self.__fuel + amount, self.__fuel_capacity)
        added = new_level - self.__fuel
        self.__fuel = new_level
        print(f"{self.brand}: Refueled {added:.2f} L (Tank: {self.__fuel:.2f}/{self.__fuel_capacity} L)")

    
    def drive(self, distance_km):
        if distance_km <= 0:
            print("Distance must be positive.")
            return

        required_fuel = distance_km * self.__consumption

        if required_fuel <= self.__fuel:
            self.__fuel -= required_fuel
            self.__odometer += distance_km
            print(f"{self.brand}: Drove {distance_km:.2f} km. Fuel used: {required_fuel:.2f} L.")
        else:
            possible_distance = self.__fuel / self.__consumption
            fuel_used = self.__fuel
            self.__odometer += possible_distance
            self.__fuel = 0.0
            print(f"{self.brand}: Ran out of fuel after {possible_distance:.2f} km (used {fuel_used:.2f} L).")

        print(f"Status -> Odometer: {self.__odometer:.2f} km | Fuel: {self.__fuel:.2f} L")

   
    def display_status(self):
        print(f"Brand: {self.brand} | Odometer: {self.__odometer:.2f} km | Fuel: {self.__fuel:.2f} L")

 
    def _set_odometer_by_mechanic(self, new_reading, auth_code):
        AUTH = "MECH2025"
        if auth_code != AUTH:
            print("Unauthorized: invalid mechanic code.")
            return
        if new_reading < 0:
            print("Invalid odometer reading.")
            return
        self.__odometer = float(new_reading)
        print(f"{self.brand}: Odometer set to {self.__odometer:.2f} km by authorized mechanic.")



cars = {}

while True:
    print("\n=== CAR SIMULATION SYSTEM ===")
    print("1. Add New Car")
    print("2. Refuel Car")
    print("3. Drive Car")
    print("4. Check Car Status")
    print("5. Mechanic Override (Odometer Reset)")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        brand = input("Enter car brand: ").strip()
        if brand in cars:
            print("This car already exists.")
        else:
            initial_fuel = float(input("Enter initial fuel (L): ") or 0)
            cars[brand] = Car(brand, fuel=initial_fuel)
            print(f"Car '{brand}' created with {initial_fuel:.2f} L of fuel.")

    elif choice == "2":
        brand = input("Enter car brand: ").strip()
        if brand in cars:
            amount = float(input("Enter amount to refuel (L): "))
            cars[brand].refuel(amount)
        else:
            print("Car not found.")

    elif choice == "3":
        brand = input("Enter car brand: ").strip()
        if brand in cars:
            distance = float(input("Enter distance to drive (km): "))
            cars[brand].drive(distance)
        else:
            print("Car not found.")

    elif choice == "4":
        if not cars:
            print("No cars available.")
        else:
            print("\n--- Car Status ---")
            for car in cars.values():
                car.display_status()

    elif choice == "5":
        brand = input("Enter car brand: ").strip()
        if brand in cars:
            new_odometer = float(input("Enter new odometer reading (km): "))
            code = input("Enter mechanic authorization code: ")
            cars[brand]._set_odometer_by_mechanic(new_odometer, code)
        else:
            print("Car not found.")

    elif choice == "6":
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")




