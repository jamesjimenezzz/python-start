def get_word():
    return "python"

def get_guesses(word_length):
    while True:
        guess = input("Enter your guess word: ")
        guess_length = len(guess)
        if guess_length != word_length:
            print(f"The word length is {word_length}. Please try again.")
            continue
        else:
           return guess


def check_guesses(guess_list, word_list, word_length):
    results = []

    for i in range(word_length):
        if guess_list[i] == word_list[i]:
            results.append("🟢")
        elif guess_list[i] in word_list:
            results.append("🟡")
        else:
             results.append("🔴")

    return results


def ask_again():
    answer = input("Do you still want to play again? y/n: ")
    return answer == "y"

def play_round(chances=5, word="python"):
    word_length = len(word)
    word_list = list(word)

    while chances > 0:
            guess = get_guesses(word_length)
            guess_list = list(guess)
            results = check_guesses(guess_list, word_list, word_length)
           
            print(results)

            if guess == word:
                print("Congratulations you won")
                break

            chances -= 1
            print(f"You only have {chances} guesses now ")



def main():
    while True:
        play_round()
        if not ask_again():
            print("Thanks for playing")
            break



main()