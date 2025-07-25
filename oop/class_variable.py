

class Student():

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name 
        self.age = age
        Student.num_students += 1



student1 = Student("James" , 17)
student2 = Student("Jamess" , 18)

print(student1.name)
print(student1.age)
print(Student.class_year)
print(Student.num_students)