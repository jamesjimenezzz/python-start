import os

file_path = "testt"

if os.path.exists(file_path):
    print("This file exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a fucking directory.")

else:
    print("This file doesn't exist.")



