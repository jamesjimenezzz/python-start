
def show_balance(balance):
    print(f"Your balance is {balance:.2f}$")


def deposit(balance):
    show_balance(balance)
    amount = int(input("Enter amount you want to deposit: "))

    if amount < 0:
        print("Invalid amount")
        return 0

    return amount

def withdraw(balance):
    show_balance(balance)

    amount = int(input("Enter the amount you want to withdraw: "))

    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < balance:
        print("Successfully withdraw")
        return amount
    else:
        print("Invalid string")


def main():
    balance = 0
    is_running = True


    while is_running:
        print("1. Show Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
          show_balance(balance)
        elif choice == 2:
            balance += deposit(balance)
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running = False
            print("Have a great day")
        else:
            print("Invalid string")



if __name__ == "__main__":
    main()