friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random
Pay_picker = random.randint(0,4)
print("Today's sucker is: ")
if Pay_picker == 0:
    print(friends[0])
elif Pay_picker == 1:
    print(friends[1])
elif Pay_picker == 2:
    print(friends[2])
elif Pay_picker == 3:
    print(friends[3])
elif Pay_picker == 4:
    print(friends[4])
