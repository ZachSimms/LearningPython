# This module looks into Lists, Tuples, Sets and Dictionaries

def lists():
    letters = ["a", "b", "c"]
    matrix = [[0, 1], [2, 3]]
    zeros = [0] * 5
    numbers = list(range(20))
    chars = list("Hello World")

    combined = zeros + letters
    print(letters)
    print(matrix)
    print(zeros)
    print(combined)
    print(numbers)
    print(chars)


def accessinglists():
    letters = ["a", "b", "c", "d"]
    numbers = list(range(20))

    print(letters[0:3])
    # Reverse order of list
    print(numbers[::-1])
    # Print every other number of list
    print(numbers[::2])


def unpackinglists():
    numbers = [1, 2, 3, 4, 5, 8, 2, 0, 0, 1]

    # Stores the first two list items into variables one and two respectively,
    # all the other list items are stored into a list called other
    one, two, *other = numbers

    first, *middle, last = numbers

    print(one)
    print(other)
    print(f"Middle Values: {middle}")
    print(f"Last Value: {last}")


def loopinglists():
    letters = ["a", "b", "c", "d"]
    # Shows enumerated key(index)/value pair for list
    for letter in enumerate(letters):
        print(letter)

    #enumerate turns list into key(index)/value pair
    for index, letter in enumerate(letters):
        print(index, letter)

loopinglists()
