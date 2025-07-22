

name = input("Enter your name: ")

while name == "":
    print("Please enter your name.")
    name = input("Enter your name: ")


print(f"Hello {name}")

#-----------------------------------------------------

num = int(input("Enter a number between 1-10 "))

while num < 1 or num > 10:
    print("Invalid Number")
    num = int(input("Enter a number between 1-10 "))


print(f"Your number is {num}")