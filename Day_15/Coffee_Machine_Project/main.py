MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("Welcome to Coffee-Maker!")
order = input("What would you like to order? Type:\n\n1: Espresso\n2: Latte\n3: Cappuccino\n").lower()

# TODO: 1. Print report of all coffee machine resources.
if order == "report" or order == "r":
    print(f"\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")

# TODO: 2. Check resources sufficient to make drink order.
elif order == "espresso" or order == "1":
    drink = MENU["espresso"]
    if resources["water"] >= drink["ingredients"]["water"] and resources["coffee"] >= drink["ingredients"]["coffee"]:
        print("Resources are sufficient to make your espresso.")
    else:
        print("Sorry, there are not enough resources to make your espresso.")
elif order == "latte" or order == "2":
    drink = MENU["latte"]
    if resources["water"] >= drink["ingredients"]["water"] and resources["milk"] >= drink["ingredients"]["milk"] and resources["coffee"] >= drink["ingredients"]["coffee"]:
        print("Resources are sufficient to make your latte.")
    else:
        print("Sorry, there are not enough resources to make your latte.")
elif order == "cappuccino" or order == "3":
    drink = MENU["cappuccino"]
    if resources["water"] >= drink["ingredients"]["water"] and resources["milk"] >= drink["ingredients"]["milk"] and resources["coffee"] >= drink["ingredients"]["coffee"]:
        print("Resources are sufficient to make your cappuccino.")
    else:
        print("Sorry, there are not enough resources to make your cappuccino.")

# TODO: 3. Process coins.
    
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))  # 0.25
    dimes = int(input("How many dimes?: "))        # 0.10
    nickels = int(input("How many nickels?: "))    # 0.05
    pennies = int(input("How many pennies?: "))    # 0.01 
    total_inserted = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    print(f"Total inserted: ${total_inserted:.2f}")
    if total_inserted >= drink["cost"]:
        change = total_inserted - drink["cost"]
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {order}. Enjoy!")
        # Deduct the used resources
        resources["water"] -= drink["ingredients"]["water"]
        if "milk" in drink["ingredients"]:
            resources["milk"] -= drink["ingredients"]["milk"]
        resources["coffee"] -= drink["ingredients"]["coffee"]
    else:
        print("Sorry, that's not enough money. Money refunded.")

# TODO: 4. Make the coffee.