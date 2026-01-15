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



player_choice = input("Welcome to the rock, paper, scissors simulator! What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors: ")
if int(player_choice) == 0:
    print(f"You chose: {rock}")
elif int(player_choice) == 1:
    print(f"You chose: {paper}")
elif int(player_choice) == 2:
    print(f"You chose: {scissors}")

import random
computer_choice = random.randint(0,2)

if computer_choice == 0:
    print(f"Computer chose: {rock}")
elif computer_choice == 1:
    print(f"Computer chose: {paper}")
elif computer_choice == 2:
    print(f"Computer chose: {scissors}")

if int(player_choice) > 2 or int(player_choice) < 0:
    print("Invalid input. You lose!")
elif int(player_choice) == 0 and computer_choice == 0:
    print("DRAW")
elif int(player_choice) == 0 and computer_choice == 1:
    print("YOU LOSE!")
elif int(player_choice) == 0 and computer_choice == 2:
    print("YOU WIN!")
elif int(player_choice) == 1 and computer_choice == 1:
    print("DRAW")
elif int(player_choice) == 1 and computer_choice == 2:
    print("YOU LOSE!")
elif int(player_choice) == 1 and computer_choice == 0:
    print("YOU WIN!")
elif int(player_choice) == 2 and computer_choice == 2:
    print("DRAW")
elif int(player_choice) == 2 and computer_choice == 0:
    print("YOU LOSE!")
elif int(player_choice) == 2 and computer_choice == 1:
    print("YOU WIN!")

# Make sure player inputs are the same as code reader inputs