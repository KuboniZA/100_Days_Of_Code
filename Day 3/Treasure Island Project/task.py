print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
First_Contact = input('Let\'s begin!\nYou are stranded on the precipice of a cliff with armed soldiers hot on your heels. Your only escape is to the "Left" or "Right"; which will you choose? ').lower()

if First_Contact == "Left" or First_Contact == "left":
    Escape = input('You speed to onwards only to be cornered by a pack of hyenas. \nType: "Option 1": Fight the creatures. '
                   '\n"Option 2": Jump into the van hurtling your way whether it has enemies or not! ').lower()
    if Escape == "Option 2".lower():
        Doors = input('Having defeated the enemies and taken over the van you come across three doors between you and freedom: '
                      '"Red", "Yellow" and "Blue". Which will you choose? ').lower()
        if Doors == "Yellow".lower():
            print("Congratulations!! You have found the treasure")
        elif Doors == "Blue".lower():
            print("GAME OVER: The soldiers have created a trap and captured you!")
        elif Doors == "Red".lower():
            print("GAME OVER: The Hyena leader has eaten you!")
        else:
            print("Error: You typed the wrong input")
    elif Escape == "Option 1".lower():
        print("GAME OVER: You ere mauled to death!")
    else:
        print("Error: You typed the wrong input")
elif First_Contact == "Right".lower():
    print("GAME OVER: Some of the soldiers flanking right have killed you!")
else:
    print("Error: You typed the wrong input")


