import random

#random_number = random.random() * 50
#print(random_number)

Selection = input('Hello and welcome to the heads or tails player!'
                  '\nSimply input "1" to select HEADS and "2" to select TAILS ')
comp_result = random.randint(1,2)
if int(comp_result) == 1:
    print("The Computer chose heads!")
    if int(Selection) == int(comp_result):
        print("Congratulations! You won!")
    else:
        print("Sorry, you lose!")
if int(comp_result) == 2:
    print("The Computer chose tails!")
    if int(Selection) == int(comp_result):
        print("Congratulations! You won!")
    else:
        print("Sorry, you lose!")