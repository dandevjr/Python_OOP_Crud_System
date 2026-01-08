class InventoryItem:
    def __init__(self, name, quantity):
        self.__name = name
        self.__quantity = quantity

    def get_name(self):  # GETTER
        return self.__name

    def set_name(self, value):  # SETTER
        self.__name = value

    def get_quantity(self):  # GETTER
        return self.__quantity

    def set_quantity(self, value):  # SETTER
        if value >= 0:
            self.__quantity = value
        else:
            print("Invalid quantity. Must be non-negative.")

    def display_details(self):
        print(f"Item: {self.__name}, Quantity: {self.__quantity}")

# Initial inventory
items = [
    InventoryItem("Mouse", 15),
    InventoryItem("Keyboard", 10)
]

# Main menu loop
while True:
    print("\nINVENTORY ITEM SYSTEM")
    print("1. View All Items")
    print("2. Add Multiple Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Encapsulation Test")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        if not items:
            print("No inventory items found.")
        else:
            for i, item in enumerate(items, start=1):  # TRAVERSAL
                print(f"{i}. ", end="")
                item.display_details()

    elif choice == "2":
        count = int(input("How many items do you want to add? "))
        for i in range(count):
            print(f"\nAdding item {i+1} of {count}")
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Error: Quantity must be non-negative.")
            else:
                items.append(InventoryItem(name, quantity))  # OBJECT CREATION
                print(f"'{name}' added successfully.")

    elif choice == "3":
        update_name = input("Enter item name to update: ")
        found = False
        for item in items:
            if item.get_name().lower() == update_name.lower():
                new_quantity = int(input("Enter new quantity: "))
                item.set_quantity(new_quantity)
                print("Item updated.")
                found = True
                break
        if not found:
            print("Item not found.")

    elif choice == "4":
        delete_name = input("Enter item name to delete: ")
        for item in items:
            if item.get_name().lower() == delete_name.lower():
                items.remove(item)
                print(f"Item '{delete_name}' deleted.")
                break
        else:
            print("Item not found.")

    elif choice == "5":  # ENCAPSULATION TEST
        for item in items:
            print(f"{item.get_name()} | Quantity: {item.get_quantity()}")

    elif choice == "6":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")