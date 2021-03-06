def agecalculator():
    birth_year = input("What is your birth year? ")
    current_year = 2020

    if int(birth_year) < current_year:
        age = current_year - int(birth_year)
        print("You are " + str(age) + " years old.")
    elif int(birth_year) == current_year:
        print("You are less than one year old. Welcome to the world!")
    else:
        age = current_year - int(birth_year)
        print("You can't be " + str(age) + " years old. Are you from the future?")


def calculator():
    first = float(input("First Number: "))
    second = float(input("Second Number: "))

    total = first + second
    print("Sum: " + str(total))


def weightconverter():
    weight = int(input("Weight: "))
    version = input("(K)g or (L)lbs: ")

    if version.upper() == "K":
        conversion = weight / 0.45
        print("Weight in lbs: " + str(conversion))
    elif version.upper() == "L":
        conversion = weight * 0.45
        print("Weight in Kg: " + str(conversion))
    else:
        print("Try again")


def eligibility():
    age = int(input("Age? "))
    # Use of ternary operator
    message = "Eligible" if age >= 19 else "Not Eligible"
    print(message)


def forelse():
    successful = True
    for number in range(3):
        print("Attempt")
        if successful:
            print("Success")
            break
    else:  # will happen if for loop fails to terminate
        print("Attempted 3 times")


def nestedForLoop():
    for x in range(5):  # for every value of x from 0-4...
        for y in range(3):  # ..there is a y value from 0-2..
            print(f"({x}, {y})")  # ..and they are printed as coordinate pairs


def iterable_objects():
    print("Range Iteration: ")
    for x in range(5):
        print(x)

    print("String Iteration: ")
    for x in "Hello":
        print(x)

    print("List Iteration: ")
    for x in ["Delta", "DEVGRU", "160th SOAR", "24th STS"]:
        print(x)


def while_loop():
    number = 100
    while number > 0:
        print(number)
        number //= 2


# Continues loop until user inputs "quit"
def while_loop2():
    command = ""
    while command.lower() != "quit":
        command = input(">")
        print("ECHO", command)


def infinite_loop():
    while True:
        command = input(">")
        print("ECHO", command)
        if command.lower() == "quit":
            break


def controlflowExercise():
    # Input range of values then print even values
    # then states how many even values are in range
    list = []
    start = int(input("Starting number of range: "))
    up_to = int(input("Up to: "))
    for x in range(start, up_to):
        if x % 2 == 0:
            list.append(x)
            print(x)
    print(f"We have {len(list)} even numbers")


def controlFlowExercisev2():
    # Input range of values then print even values
    # then states how many even values are in range
    count = 0
    start = int(input("Starting number of range: "))
    up_to = int(input("Up to: "))
    for x in range(start, up_to):
        if x % 2 == 0:
            count += 1
            print(x)
    print(f"We have {count} even numbers")


def masmultiply(*numbers):
    # Takes in parameter of several numbers and produces
    # the product of all numbers together

    total = 1
    for x in numbers:
        total *= x
    return total


def save_user(**user):
    print(user)
    print(user["name"])

    # to run:
    # save_user(id = 1, name = "John", age = 22)


def fizz_buzz(input):
    # Fizz Buzz function exercise
    # If divisible by 3 -> Fizz
    # If divisible by 5 -> Buzz
    # If divisible by 3 and 5 -> FizzBuzz
    # Any other -> echo back input

    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(7))
