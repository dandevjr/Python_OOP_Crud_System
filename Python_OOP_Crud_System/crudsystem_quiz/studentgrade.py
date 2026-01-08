class Student:
    def __init__(self, name, course):  
        self.name = name              
        self.course = course          
        self.__prelim = 0             
        self.__midterm = 0            
        self.__final = 0             

    
    def get_prelim(self):
        return self.__prelim

    def get_midterm(self):
        return self.__midterm

    def get_final(self):
        return self.__final

    
    def set_prelim(self, score):
        if 0 <= score <= 100:
            self.__prelim = score
        else:
            print("Invalid prelim score. Must be 0–100.")

    def set_midterm(self, score):
        if 0 <= score <= 100:
            self.__midterm = score
        else:
            print("Invalid midterm score. Must be 0–100.")

    def set_final(self, score):
        if 0 <= score <= 100:
            self.__final = score
        else:
            print("Invalid final score. Must be 0–100.")

    
    def get_final_average(self):
        return round((self.__prelim + self.__midterm + self.__final) / 3, 2)

    def get_remark(self):
        return "Passed" if self.get_final_average() >= 75 else "Failed"

   
    def display_info(self):
        print(f"Name: {self.name}, Course: {self.course}")
        print(f"Prelim: {self.__prelim}, Midterm: {self.__midterm}, Final: {self.__final}")
        print(f"Final Average: {self.get_final_average()}, Remark: {self.get_remark()}\n")


class Gradebook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all(self):
        for student in self.students:
            student.display_info()

    def compute_class_average(self):
        if not self.students:
            print("No students in gradebook.")
            return
        total = sum(student.get_final_average() for student in self.students)
        class_avg = round(total / len(self.students), 2)
        print(f"Class Average: {class_avg}")


    def list_top_performers(self):
        top = [s for s in self.students if s.get_final_average() >= 90]
        print("Top Performers:")
        for student in top:
            print(f"{student.name} - {student.get_final_average()}")


s1 = Student("Richie ", "BSIT")
s1.set_prelim(85)
s1.set_midterm(90)
s1.set_final(88)

s2 = Student("Dalan", "BSIT")
s2.set_prelim(70)
s2.set_midterm(65)
s2.set_final(60)

s3 = Student("Mitch", "BSIT")
s3.set_prelim(95)
s3.set_midterm(92)
s3.set_final(96)


print("\nWelcome to Student Grade:")
print("\nAdd a new student:")
name_input = input("Enter student name: ")
course_input = input("Enter course: ")
prelim_input = int(input("Enter prelim score (0–100): "))
midterm_input = int(input("Enter midterm score (0–100): "))
final_input = int(input("Enter final score (0–100): "))

user_student = Student(name_input, course_input)
user_student.set_prelim(prelim_input)
user_student.set_midterm(midterm_input)
user_student.set_final(final_input)


gradebook = Gradebook()
gradebook.add_student(s1)
gradebook.add_student(s2)
gradebook.add_student(s3)
gradebook.add_student(user_student)

gradebook.display_all()
gradebook.compute_class_average()
gradebook.list_top_performers()



print("\nEncapsulation Test:")
if prelim_input == user_student.get_prelim():
    print("Prelim score is access")
else:
    print("Prelim score is invalid")
if midterm_input == user_student.get_midterm():
    print("midterm score is access")
else:
    print("midterm score is invalid")
if final_input == user_student.get_final():
    print("final score is access")
else:
    print("final score is invalid")