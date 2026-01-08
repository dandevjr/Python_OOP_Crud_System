from reservation import Reservation

class ReservationSystem:
    def __init__(self):
        self.reservations = []

    def create_multiple_reservations(self):
        try:
            count = int(input("How many reservations to create? "))
            for i in range(count):
                print(f"\nCreating reservation #{i+1}")
                name = input("Enter passenger name: ")
                flight = input("Enter flight number: ")
                seat = input("Enter seat number: ")
                self.reservations.append(Reservation(name, flight, seat))
            print(f" {count} reservations created.")
        except ValueError:
            print("Invalid number.")

    def view_reservations(self):
        if not self.reservations:
            print("No reservations found.")
        else:
            print("\n Current Reservations:")
            for i, r in enumerate(self.reservations, start=1):
                print(f"{i}. ", end="")
                r.display()

    def update_reservation(self):
        self.view_reservations()
        try:
            index = int(input("Enter reservation number to update: ")) - 1
            if 0 <= index < len(self.reservations):
                name = input("New passenger name: ")
                flight = input("New flight number: ")
                seat = input("New seat number: ")
                r = self.reservations[index]
                r.set_passenger_name(name)
                r.set_flight_number(flight)
                r.set_seat_number(seat)
                print(" Reservation updated.")
            else:
                print(" Invalid reservation number.")
        except ValueError:
            print(" Please enter a valid number.")

    def delete_reservation(self):
        self.view_reservations()
        try:
            index = int(input("Enter reservation number to delete: ")) - 1
            if 0 <= index < len(self.reservations):
                del self.reservations[index]
                print(" Reservation deleted.")
            else:
                print(" Invalid reservation number.")
        except ValueError:
            print(" Please enter a valid number.")

    def test_encapsulation(self):
        print("\n Encapsulation Test")
        for i, r in enumerate(self.reservations, start=1):
            print(f"{i}. Passenger: {r.get_passenger_name()} | Flight: {r.get_flight_number()} | Seat: {r.get_seat_number()}")

    def run(self):
        while True:
            print("\n Airplane Seat Reservation System")
            print("1. Create Multiple Reservations")
            print("2. View All Reservations")
            print("3. Update Reservation")
            print("4. Delete Reservation")
            print("5. Encapsulation Test")
            print("6. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.create_multiple_reservations()
            elif choice == '2':
                self.view_reservations()
            elif choice == '3':
                self.update_reservation()
            elif choice == '4':
                self.delete_reservation()
            elif choice == '5':
                self.test_encapsulation()
            elif choice == '6':
                print(" Exiting system...")
                break
            else:
                print(" Invalid choice.")

if __name__ == "__main__":
    system = ReservationSystem()
    system.run()