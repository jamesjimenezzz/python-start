

questions = ("How many elements are in the periodic table?", "Which animal lays the largest eggs? ", "What is the most abundant gas in Earth's atmosphere?", "How many bones are in the human body?", "Which planet in the solar system is the hottest? ")


options = (("A. 116", "B.117", "C.118", "D.119"),  ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),("A. 206", "B. 207", "C. 208", "D. 209"), ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))


answers = ("C", "D", "A", "A", "B")
guesses = []


numSort = 0
score =0

for question in questions:
    print("-----")
    print(question)
    for option in options[numSort]:
        print(option)
    
   
    guess = input("What is your answer? ")
    guesses.append(guess.upper())
    if guess.upper() == answers[numSort]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
   
    numSort += 1


percentage = round((score / len(questions))* 100 )
print(f"Your score percentage is {percentage}%")
   

    
