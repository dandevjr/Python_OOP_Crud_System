class Student:
    def __init__(self, name, student_id, course):
        self.__name = name
        self.__student_id = student_id
        self.__course = course

    def get_name(self):  # GETTER
        return self.__name

    def set_name(self, value):  # SETTER
        self.__name = value

    def get_id(self):  # GETTER
        return self.__student_id

    def set_id(self, value):  # SETTER
        self.__student_id = value

    def get_course(self):  # GETTER
        return self.__course

    def set_course(self, value):  # SETTER
        self.__course = value

    def display_details(self):
        print(f"Name: {self.__name}, ID: {self.__student_id}, Course: {self.__course}")

students = [
    Student("Jack", "2023001", "BSIT"),
    Student("Romar", "2023002", "BSCS")
]

while True:
    print("\nSTUDENT INFORMATION SYSTEM")
    print("1. View All Students")
    print("2. Add New Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Encapsulation Test")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        if not students:
            print("No student records found.")
        else:
            for i, s in enumerate(students, start=1):  # TRAVERSAL
                print(f"{i}. ", end="")
                s.display_details()

    elif choice == "2":
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        course = input("Enter course: ")
        students.append(Student(name, student_id, course))  # OBJECT CREATION
        print(f"'{name}' added successfully.")

    elif choice == "3":
        update_id = input("Enter student ID to update: ")
        found = False
        for s in students:
            if s.get_id() == update_id:
                new_name = input("Enter new name: ")
                new_course = input("Enter new course: ")
                s.set_name(new_name)
                s.set_course(new_course)
                print("Student updated.")
                found = True
                break
        if not found:
            print("Student ID not found.")

    elif choice == "4":
        delete_id = input("Enter student ID to delete: ")
        for s in students:
            if s.get_id() == delete_id:
                students.remove(s)
                print(f"Student with ID '{delete_id}' deleted.")
                break
        else:
            print("Student ID not found.")

    elif choice == "5":  # ENCAPSULATION TEST
        for s in students:
            print(f"{s.get_name()} | ID: {s.get_id()} | Course: {s.get_course()}")

    elif choice == "6":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")