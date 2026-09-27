class Student:
    def __init__(self, student_id, name, course, age):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.age = int(age)

    def show(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Course: {self.course} | Age: {self.age}")


def show_youngest_student(students):
    if not students:
        print("ไม่มีข้อมูลนักเรียน")
        return

    youngest = min(students, key=lambda s: s.age)
    
    print("=== นักเรียนที่มีอายุน้อยที่สุด ===")
    youngest.show()


students_list = []

with open("Lab/Lab8-1/students.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line:
            student_id, name, course, age = line.split(",")

            student_obj = Student(student_id, name, course, age)
            students_list.append(student_obj)

show_youngest_student(students_list)