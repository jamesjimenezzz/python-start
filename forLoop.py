
import time

for i in reversed(range(1,11)):
    print(i)
    time.sleep(0.5)

print("Happy new year!")



#for i in range(10):
 #   print(i + 1) #1 2 3 4 - 10


rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))
symbol = input("Enter symbol: ")


for i in range(rows):
    for j in range(columns):
        print(symbol, end="")

    print()


#@@@@
#@@@@
#@@@@






for i in range(21):
    if i == 13:
        continue
    else:
        print(i)