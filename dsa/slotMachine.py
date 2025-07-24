
import random

def spin_row():
    slots = ["🍕", "🍔", "🍟"]
    
    return [random.choice(slots) for _ in range(3)]

   
def print_row(row):
     print(" ".join(row))


def get_payload(row, amount):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍕":
            return amount * 2
        elif row[0] == "🍔":
            return amount * 4
        elif row[0] == "🍟":
            return amount * 5

    else:
        return 0
    
    
def main():
    is_running = True
    balance = 100

    print("Welcome to python slots")
    print("Symbols: 1, 2, 3 ,4")
    print("*************************")
    while is_running:
       
        print(f"Current balance: {balance}$")
        amount = (input("Place your bet amount: "))
        
        if not amount.isdigit():
            print("Please enter a number")
           
        

        amount = int(amount)
        if amount > balance:
            print(f"Insufficient balance")
            continue
            

        if amount <= 0:
            print("Bet must be greater than 0")

        row = spin_row()
       
        print_row(row)

        payout = get_payload(row, amount)
      

        if payout > 0:
            print("You won")
        else:
            print("You lost")

        
        balance += payout


        balance -= amount

        decide = input("Do you still want to play? y/n ")
        if decide.lower() != "y":
            is_running = False
        else:
            continue

    print("Thanks for playing!")
          


main()


       




