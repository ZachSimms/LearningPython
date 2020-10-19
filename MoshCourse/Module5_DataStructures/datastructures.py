# This module looks into Lists, Tuples, Sets and Dictionaries
# letters = ["a", "b", "c", "d"]
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

    # enumerate turns list into key(index)/value pair
    for index, letter in enumerate(letters):
        print(index, letter)


def addremovelists():
    # Add
    letters = ["a", "b", "c"]
    letters.append("d")  # add to end of list
    letters.insert(0, "-")  # add to specific place
    print(letters)

    # Remove
    names = ["Peter", "Marcus", "Ray", "Malcolm"]
    names.pop()  # remove last item
    names.pop(0)  # remove at specific index
    names.remove("Ray")
    # del names[0:3]
    # letters.clear()
    print(names)


def findingitems():
    letters = ["a", "b", "c", "c", "z"]
    print(letters.index("a"))
    print(letters.count("c"))

    if "d" in letters:
        print(letters.index("d"))


def sortinglistsOne():
    numbers = [3, 51, 2, 8, 6]
    numbers.sort()  # modifies original list
    print(numbers)

    numbers2 = [3, 51, 2, 8, 6]
    numbers2.sort(reverse=True)  # modifies original list
    print(numbers2)

    ascending = sorted(numbers)  # Sorted does not change original list
    decending = sorted(numbers, reverse=True)
    print(ascending)
    print(decending)


def sortinglistsTwo():
    items = [
        ("Product1", 10),
        ("Product2", 9),
        ("Product3", 12)
    ]

    def sort_item(item):
        return item[1]  # Returns prices

    items.sort(key=sort_item)  # Sort by price
    print(items)


def lambdafunction():
    items = [
        ("Product1", 10),
        ("Product2", 9),
        ("Product3", 12)
    ]

    items.sort(key=lambda item: item[1])  # lambda parameters:expression
    print(items)


def mapfunctions():
    items = [
        ("Product1", 10),
        ("Product2", 9),
        ("Product3", 12)
    ]

    x = map(lambda item: item[1], items) # Will call the lambda function on each item of iterable items
    for item in x:
        print(item)

def anotherlambda(n):
  return lambda a : a * n
# mydoubler = myfunc(2)
# print(mydoubler(11))

