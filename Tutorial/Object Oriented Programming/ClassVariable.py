# Class Variable = Shared among all instances of a class
#                  Defined outside the constructor
#                  Allow you to share data among all objects created from that class

class Student:

    class_year = 2025 # Class Variable 1
    num_student = 0   # Class Variable 2

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Sandy", 25)
student4 = Student("Squidward", 40)

print(Student.num_student)
print(f"My graduating class of {Student.class_year} has {Student.num_student} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)