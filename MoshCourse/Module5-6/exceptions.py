def exceptions():
    try:
        age = int(input("Age: "))
    except ValueError as ex: # input a letter
        print("You didn't enter a valid age.")
        print(f'Error: {ex}')
        print(f"Error Type: {type(ex)}")
    else: # input a number
        print("No exceptions were thrown")
    print("Execution continues")


def exceptionv2():
    try:
        age = int(input("Age: "))
        xfactor = 10/age
    except (ValueError, ZeroDivisionError):
        print("You didn't enter a valid age.")
    else: # input a number
        print("No exceptions were thrown")

def cleanup():
    try:
        file = open("datastructures.py")
        age = int(input("Age: "))
        xfactor = 10/age
        file.close()
    except (ValueError, ZeroDivisionError):
        print("You didn't enter a valid age.")
    else: # input a number
        print("No exceptions were thrown")
    finally: # Ran if error or not. Used to release and close things.
        file.close()

def withstatement():
    try:
        # With statement will automatically close files
        # Good for releasing files
        with open("datastructures.py") as file, open("exceptions.py") as target:
            # Can work with file here
            print('file opened')
            # file.__exit__()
        age = int(input("Age: "))
        xfactor = 10/age
    except (ValueError, ZeroDivisionError):
        print("You didn't enter a valid age.")
    else:
        print("No exceptions were thrown")


def calculate_xfactor(age):
    # Google 'python 3 built-in exceptions'
    # Technique not advised, but will see in other's code
    if age <= 0:
        raise ValueError("Age can't be 0 or less.")
    return 10/age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)

from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can't be 0 or less.")
    return 10/age
    

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

# Cleaner way without raising an exception
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age



xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass

"""
#Execution time of code after 10000 repetitions
print('First code: ', timeit(code1, number=10000))
print('Second code: ', timeit(code2, number=10000))