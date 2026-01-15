print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    Age = int(input("What is your age? "))
    if Age <= 12:
        print("Pay $5")
    elif Age <= 18:
        print("Pay $7")
    elif Age > 18:
        print("pay $10")
else:
    print("Sorry you have to grow taller before you can ride.")
