

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Web Dev", "Full Stack Dev", "Web Designer"]
        return position in valid_positions



employee1 = Employee("James", "Full Stack Dev")

print(employee1.is_valid_position(employee1.position))