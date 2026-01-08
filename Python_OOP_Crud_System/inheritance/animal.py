class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):  # GETTER
        return self.__name

    def set_name(self, value):  # SETTER
        self.__name = value

    def make_sound(self):
        print(f"{self.__name} makes a generic animal sound.")

    def display_details(self):
        print(f"Animal: {self.__name}")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.get_name()} says Meow.")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.get_name()} says Woof.")

animals = [
    Cat("Whiskers"),
    Dog("Buddy"),
    Animal("Unknown")
]

while True:
    print("\nANIMAL SOUND SYSTEM")
    print("1. View All Animals")
    print("2. Add New Animal")
    print("3. Update Animal Name")
    print("4. Delete Animal")
    print("5. Make All Sounds")
    print("6. Encapsulation Test")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "1":
        if not animals:
            print("No animals found.")
        else:
            for i, a in enumerate(animals, start=1):  # TRAVERSAL
                print(f"{i}. ", end="")
                a.display_details()

    elif choice == "2":
        name = input("Enter animal name: ")
        kind = input("Type (Cat/Dog/Other): ").strip().lower()
        #  OBJECT CREATION
        if kind == "cat":
            animals.append(Cat(name))
        elif kind == "dog":
            animals.append(Dog(name))
        else:
            animals.append(Animal(name))
        print(f"{name} added as {kind.title()}.")

    elif choice == "3":
        index = int(input("Enter animal number to update: ")) - 1
        if 0 <= index < len(animals):
            new_name = input("Enter new name: ")
            animals[index].set_name(new_name)
            print("Animal name updated.")
        else:
            print("Invalid selection.")

    elif choice == "4":
        index = int(input("Enter animal number to delete: ")) - 1
        if 0 <= index < len(animals):
            removed = animals.pop(index)
            print(f"{removed.get_name()} deleted.")
        else:
            print("Invalid selection.")

    elif choice == "5":
        for a in animals:
            a.make_sound()

    elif choice == "6":  # ENCAPSULATION TEST
        for a in animals:
            print(f"Access: {a.get_name()}")

    elif choice == "7":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")