print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#(150*1.1)/2
tip_amount = bill / 100 * tip
print(tip_amount)
Share  = round((bill + tip_amount) / people, 2)
print(f"\nEach person should pay: ${Share}")