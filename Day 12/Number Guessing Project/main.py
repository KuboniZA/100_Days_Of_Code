from art import logo
import random
print(logo)
computer_number = random.randint(1, 100)

print("Welcome to iNumba Numba!! The internets number one number guessing game!")
print("I'm thinking of a number between 1 and 100.")
game_difficulty = input("Choose difficulty: Type 'easy' or 'hard'\n").lower()
game_status = True

def gameplay():
    game_over = False
    easy_attempts_left = 10
    hard_attempts_left = 5
    if game_difficulty == "easy":
        print(f"You have {easy_attempts_left} attempts left.")
        guess = int(input("Make a guess:\n"))
        while not game_over:
            easy_attempts_left -= 1
            if guess > computer_number and easy_attempts_left > 0:
                print(f"You have {easy_attempts_left} attempts left.")
                guess = int(input("Your number is too high. Please guess again?\n"))
            elif guess < computer_number and easy_attempts_left > 0:
                print(f"You have {easy_attempts_left} attempts left.")
                guess = int(input("Your number is too low. Please guess again?\n"))
            elif guess == computer_number:
                game_over = True
                print("You guessed right! 😃 YOU WIN! 😎\nRefresh the page to go again.")
            elif easy_attempts_left == 0:
                game_over = True
                print(f"You have {easy_attempts_left} attempts left.")
                print("Game over: 😫 YOU LOSE! 😭\nRefresh the page to go again.")
    elif game_difficulty == "hard":
        print(f"You have {hard_attempts_left} attempts left.")
        guess = int(input("Make a guess: "))
        while not game_over:
            hard_attempts_left -= 1
            if guess > computer_number and hard_attempts_left > 0:
                print(f"You have {hard_attempts_left} attempts left.")
                guess = int(input("Your number is too high. Please guess again?\n"))
            elif guess < computer_number and hard_attempts_left > 0:
                print(f"You have {hard_attempts_left} attempts left.")
                guess = int(input("Your number is too low. Please guess again?\n"))
            elif guess == computer_number:
                game_over = True
                print("You guessed right! 😃 YOU WIN! 😎\nRefresh the page to go again.")
            elif hard_attempts_left == 0:
                game_over = True
                print(f"You have {hard_attempts_left} attempts left.")
                print("Game over: 😫 YOU LOSE! 😭\nRefresh the page to go again.")

if game_difficulty == "easy" or game_difficulty == "hard":
    gameplay()
else:
    game_status = False
    while game_status != True:
        print("Invalid selection. Please try again?")
        game_difficulty = input("Choose difficulty: Type 'easy' or 'hard'\n").lower()
        if game_difficulty == "easy" or game_difficulty == "hard":
            gameplay()