class Person:
    def __init__(self, name, address, weight, height):
        self.name = name
        self.address = address
        self.weight = weight
        self.height = height

    def show(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} cm")

    def getBMI(self):
        bmi = self.weight / ((self.height / 100) ** 2)
        return bmi

class Student(Person):
    def __init__(self, name, address, weight, height, student_id, course, gpa):
        super().__init__(name, address, weight, height)
        self.student_id = student_id
        self.course = course
        self.gpa = gpa

    def show(self):
        super().show()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")
        print(f"GPA: {self.gpa}")
        print(f"BMI: {super().getBMI():.2f}")

class Employee(Person):
    def __init__(self, name, address, weight, height, employee_id, department, salary):
        super().__init__(name, address, weight, height)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def show(self):
        super().show()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        print(f"BMI: {super().getBMI():.2f}")

print("--- ข้อมูลนักเรียน ---")
student = Student("สมชาย", "123 กรุงเทพฯ", 63.5, 177, "ST66001", "Cpr.E", 3.75)
student.show()

print("\n--- ข้อมูลพนักงาน ---")
employee = Employee("สมหญิง", "456 นนทบุรี", 52.0, 160, "EMP1001", "IT Support", 35000)
employee.show()