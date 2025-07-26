

class Student:

    count = 0
    total_gpa = 0 

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count +=1
        Student.total_gpa += gpa

    
    def get_info(self):
        return f"{self.name}, {self.gpa}"


    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def get_average(cls):
        x = cls.total_gpa
        y = cls.count
        z = x / y

        if y == 0:
            return 0
        else:
            return f"The average gpa of the students here is {z}"


student1 = Student("James", 17)
student1 = Student("James", 17)

print(Student.get_average())