


students = {"James": "A", "Emman": "B", "Simon": "C"}


student = input("Enter the name of the student: ")


if student in students:
    print(f"{student} is a student and his grade is {students[student]}")
else:
    print(f"{student} is not found")




email = "asunahaley@gmail.com"

if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")