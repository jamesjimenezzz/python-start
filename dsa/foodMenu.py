

menu = {"pizza" : 3, "nachos": 4, "popcorn": 6, "fries": 2.50}
cart = []
total = 0


print("-----------MENU----------")
for key, value in menu.items():
    print(f"{key:10}: {value}")


print("-------------------------")

while True:
    item = input("What do you want on the menu? (q to exit) ")
    if item.lower() == "q":
        break
    elif menu.get(item) is not None:
        cart.append(item)
    



for food in cart:
    total = total + menu.get(food)
  
   




print(f"Your orders are {",".join(cart)}")
print(f"the total is {total}$")
    