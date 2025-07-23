import random

options = ("rock", "paper", "scissors")
computer = random.choice(options)

playing = True


while playing:
  
    player = None
    if player not in options:
        player = input("Choose one option (rock, paper, or scissors)? (q to quit): ")
        
    
    if player.lower() == "q":
        print("Thanks for playing !")
        break


    if player == computer:
        print("Its a tie")
    
    elif player == "rock" and computer == "scissors" or player == "scissors" and computer == "paper" or player == "paper" and computer == "rock":
        print("You won !")
    
    else:
        print("You lost!")
    
    print(f"Player: {player}")
    print(f"Computer {computer}")


    play_again = input("Want to play again? (y to play again, q to quit)")
    
    if play_again.lower() != "y":
        print("Thanks for playing!")
        playing = False