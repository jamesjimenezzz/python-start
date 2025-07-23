
import random


low = 1
high = 2

randomNumber = random.randint(low, high)



while True:
    guess = int(input("Enter the number of your guess between 1-2: "))
    if guess >=1 and guess <=100:
        if guess == randomNumber:
            print("Congrats you won!")
            break
        else:
            print(f"The random number is {randomNumber}")
    else:
        print("Only numbers 1-100")


    print(guess)
