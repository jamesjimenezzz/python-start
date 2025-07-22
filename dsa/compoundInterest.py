


while True:
    principle = float(input("Enter principle: "))
    if principle < 0:
        print("Principle must not be less than 0.")
    else:
        break

while True:
    rate = float(input("Enter rate: "))
    if rate < 0:
        print("Rate must not be less than 0.")
    else:
        break

while True:
    time = float(input("Enter time: "))
    if time < 0:
        print("Time must not be less than 0.")
    else: 
        break


finalAmount = principle * pow((1 + rate / 100 ), time)
roundedAmount =  (f"{finalAmount:.2f}")


print(roundedAmount)