def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculation():
    should_continue = True
    operators = {"+": add, "-": subtract, "*": multiply, "/": divide}

    from art import logo
    print(logo)
    starting_number = int(input("Please type in the first number?\n"))

    while should_continue == True:
        print("OPERATORS:\n* for multiply\n/ for divide\n+ for addition\n- for subtraction\n")
        operation = input("Select an operation from the list above?\n")
        second_number = int(input("Please type in another number?\n"))
        answer = operators[operation](starting_number,second_number)
        print(f"The answer is {answer}")
        keep_going = input("Would you like to continue? Type 'y' for yes and 'n' for no.\n").lower()
        if keep_going == "n":
            should_continue = False
            print("Thank you for using our calculator today.")
        else:
            starting_number = answer
calculation()

# def calculator():
#     print(art.logo)
#     should_accumulate = True
#     num1 = float(input("What is the first number?: "))
#
#     while should_accumulate:
#         for symbol in operations:
#             print(symbol)
#         operation_symbol = input("Pick an operation: ")
#         num2 = float(input("What is the next number?: "))
#         answer = operations[operation_symbol](num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
#
#         choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
#
#         if choice == "y":
#             num1 = answer
#         else:
#             should_accumulate = False
#             print("\n" * 20)
#             calculator()
#
#
# calculator()