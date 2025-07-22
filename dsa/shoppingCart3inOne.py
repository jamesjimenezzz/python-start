foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() != "q":
       price = float(input(("Enter the price of the food: ")))
       foods.append(food)
       prices.append(price)
    else: 
        break

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price


print(f"the total price of your cart is {total}")
    