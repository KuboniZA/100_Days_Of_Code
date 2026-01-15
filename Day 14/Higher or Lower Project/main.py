import random
from game_data import data
game_over = False
score = 0
name1 = (random.choice(data))
choice1_name = name1["name"]
choice1_description = name1["description"]
choice1_location = name1["country"]
choice1_calculator = name1["follower_count"]

while not game_over:
    name2 = (random.choice(data))
    if name1 == name2:
        name2 = (random.choice(data))
    choice2_name = name2["name"]
    choice2_description = name2["description"]
    choice2_location = name2["country"]
    choice2_calculator = name2["follower_count"]

    from art import logo
    print(logo)
    print(f"Most searched A: {choice1_name}, a {choice1_description} from {choice1_location}.")

    from art import vs
    print(vs)
    print(f"Most searched B: {choice2_name}, a {choice2_description} from {choice2_location}.")
    print(f"\nYour current score is: {score}")
    user_calculator = ""
    computer_calculator = ""
    user_selection = input("\nWho has more followers? Type 'A' or 'B':\n").lower()
    if user_selection == "a":
        user_calculator = choice1_calculator
        computer_calculator = choice2_calculator

        if computer_calculator > user_calculator:
            game_over = True
            print("That is incorrect. 😫YOU LOSE 😭\n\nRefresh to start again.")
        else:
            score += 1
            print("\n" * 20)
    elif user_selection == "b":
        user_calculator = choice1_calculator
        computer_calculator = choice2_calculator
        if computer_calculator > user_calculator:
            game_over = True
            print("That is incorrect. 😫YOU LOSE 😭\n\nRefresh to start again.")
        else:
            score += 1
            choice1_name = choice2_name
            choice1_description = choice2_description
            choice1_location = choice2_location
            user_calculator = choice2_calculator
            print("\n" * 20)
