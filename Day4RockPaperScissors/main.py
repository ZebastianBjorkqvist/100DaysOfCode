import random
import datetime

random.seed(datetime.datetime.now())

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def print_symbol(c):
    if c == 0:
        print(rock)
    elif c == 1:
        print(paper)
    elif c == 2:
        print(scissors)


playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print_symbol(playerChoice)

pcChoice = random.randint(0, 2)
print("Computer choose")
print_symbol(pcChoice)

if playerChoice > 2 or playerChoice < 0:
    print("Invalid choice")
elif playerChoice == pcChoice:
    print("No one wins")
else:
    if playerChoice == 0:
        if pcChoice == 1:
            print("You lose")
        elif pcChoice == 2:
            print("You win")
    elif playerChoice == 1:
        if pcChoice == 0:
            print("You win")
        elif pcChoice == 2:
            print("You lose")
    elif playerChoice == 2:
        if pcChoice == 0:
            print("You lose")
        elif pcChoice == 1:
            print("You win")

