import math

item = input("What item do you want? ")
price = float(input(f"How much is {item}? "))
quantity = int(input(f"How many {item}s do you want?"))

totalPrice = round(price * quantity, 2)



print(f"The total price of {item} with {quantity} quantities is {totalPrice}")
