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

import random
RandRPSNum = random.randint(0, 2)
RandRPS = ["rock", "paper", "scissors"]
CRPS = RandRPS[RandRPSNum]
#Computers RPS Choice ^^^^

print("Welcome to Beans1..... ROCK, PAPER, SCISSORS!!!")
PC = input("rock, paper, scissors... SHOOT! (Use 0, 1, 2 for Rock, Paper, Scissors) :")
#Intro and players choice^^^^
print()
print()

if PC == "0" and CRPS == "rock":
    print("Draw!")
    print('''
    You: Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''          )
    print('''
    CPU: Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

elif PC == "0" and CRPS == "paper":
    print("Lost!")
    print(''' 
    You: Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    print('''
    CPU: Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

elif PC == "0" and CRPS == "scissors":
    print("Won!")
    print('''
    You: Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    print('''
    CPU: Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

elif PC == "1" and CRPS == "rock":
    print("Won!")
    print('''
    You: Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    print('''
    CPU: Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

elif PC == "1" and CRPS == "paper":
    print("Draw!")
    print('''
    You: Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    print('''
    CPU: Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

elif PC == "1" and CRPS == "scissors":
    print("Lost!")
    print('''
    You: Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    print('''
    CPU: Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

elif PC == "2" and CRPS == "rock":
    print("Lost!")
    print('''
    You: Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    print('''
    CPU: Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

elif PC == "2" and CRPS == "paper":
    print("Won!")
    print('''
    You: Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    print('''
    CPU: Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

elif PC == "2" and CRPS == "scissors":
    print("Draw!")
    print('''
    You: Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    print('''
    CPU: Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

else:
    print("Not a valid selection")

#All the possible outcomes^^^^

print("Good Game!!")



