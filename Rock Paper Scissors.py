
#Jed Johnson
#9/9/2020
import random

words = ["Rock", "Paper", "Scissors"]
rand = random.choice(words)
line = input("choose rock paper or scissors: ")


line = line.strip()
line = line.lower()


if line == "rock":
    print(rand)

elif line == "paper":
    print(rand)
    
elif line == "scissors":
    print(rand)





else:
    print("Ah were playing rock paper scissors the word you gave me does not compute")
