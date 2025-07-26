

txt_data="I Like Pizzas!"

file_path="output.txt"

try:
    with open(file_path, "a") as file:
        file.write(f"\n {txt_data}")
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("That file already exists")