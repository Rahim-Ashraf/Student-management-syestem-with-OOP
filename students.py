class StudentDatabase:
    student_list = []
    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)
    @classmethod
    def find_student_by_id(cls, student_id):
        for student in cls.student_list:
            if student._Student__student_id == student_id:
                return student
        return None
    @classmethod
    def view_all_students(cls):
        for student in cls.student_list:
             print(student.view_student_info())

class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
    def __repr__(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrolled: {self.__is_enrolled}"
    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f"Student {self.__name} has been enrolled.")
        else:
            print(f"Student {self.__name} is already enrolled.")

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f"Student {self.__name} has been dropped.")
        else:
            print(f"Student {self.__name} is not enrolled.")

    def view_student_info(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrolled: {self.__is_enrolled}"
        
alice = Student("S101", "Alice Smith", "Computer Science", False)
bob = Student("S102", "Bob Johnson", "Mathematics", False)
charlie = Student("S103", "Charlie Lee", "Physics", False)
StudentDatabase.add_student(alice)
StudentDatabase.add_student(bob)
StudentDatabase.add_student(charlie)

while True:
    print("\n--- Student Management Menu ---")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        StudentDatabase.view_all_students()
    elif choice == '2':
        student_id = input("Enter Student ID to enroll: ")
        student = StudentDatabase.find_student_by_id(student_id)
        if student:
            student.enroll_student()
        else:
            print("Student not found.")

    elif choice == '3':
        student_id = input("Enter Student ID to drop: ")
        student = StudentDatabase.find_student_by_id(student_id)
        if student:
            student.drop_student()
        else:
            print("Student not found.")

    elif choice == '4':
        break