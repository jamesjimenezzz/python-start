

is_running = True
balance = 0


def deposit():
    amount = int(input("Enter the amount you want to deposit: "))
    print(f"You withdrawed {amount}")
    return amount

while is_running:
    balance += deposit()
    print(balance)
    




