

import random

rps = ("rock", "paper", "scissors")
rpsList = ["rock", "paper", "scissors", "idk", "hey"]



choice = random.choice(rps)
print(choice)



#------#
choice = random.shuffle(rpsList)

print(rpsList)