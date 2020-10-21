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
    prices = list(map(lambda item: item[1], items))  # Will call the lambda function on each item of iterable items
    print(prices)
    # [10, 9, 12]


def filterfunction():
    items = [
        ("Product1", 10),
        ("Product2", 9),
        ("Product3", 12)
    ]

    x = list(filter(lambda item: item[1] >= 10, items))
    print(x)
    # prints list of products with prices >= 10.


def listcomprehensions():
    items = [
        ("Product1", 10),
        ("Product2", 9),
        ("Product3", 12)
    ]

    # Both lines do the same thing
    prices = list(map(lambda item: item[1], items))
    prices = [item[1] for item in items]

    # Both lines do the same thing
    filtered = list(filter(lambda item: item[1] >= 10, items))
    filtered = [item for item in items if item[1] >= 10]


def zipfunction():
    list1 = [1, 2, 3]
    list2 = [10, 20, 30]

    print(list(zip(list1, list2)))
    print(list(zip("abc", list1, list2)))


def stacks():
    # Refering to stack of items
    # Remove from stop of stack; LIFO - Las In - First Out
    # List clicking the back button in a browers. Go back to most recent site(item on stack)

    browsing_session = []
    browsing_session.append("first site")  # Add items onto the top of stack
    browsing_session.append("second site")
    browsing_session.append("final site")
    print(browsing_session)
    last = browsing_session.pop()  # Get rid of the most recent item of stack
    print(last)
    print(browsing_session)
    if not browsing_session:  # Check to see if there is another item in stack.
        print("redirect", browsing_session[-1])  # Get the next item on top of stack


from collections import deque


def queue():
    # Reverse of the Stack
    # FIFO system

    queue = deque([])
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print(queue)
    queue.popleft()
    print(queue)
    if not queue:
        print("empty")


def tuples():
    point = (1, 2)
    pointb = 1, 2
    pointc = 1,
    pointd = ()
    print(f"Types: {type(point)}, {type(pointb)}, {type(pointc)}, {type(pointd)}")

    pointe = (1, 2) + (8, 9)
    pointf = (1, 2) * 3
    print(pointe)
    print(pointf)

    pointg = (1, 3, 8)
    x, y, z = pointg
    if 10 in pointg:
        print("exists")
    else:
        print("no exists")

    pointh = tuple("Hello World")
    print(pointh)


def swapping_vars():
    x = 10
    y = 11
    print(f'{x}, {y}')
    x, y = y, x
    print(f'{x}, {y}')


from array import array


def arrays():
    # Arrays are like lists, but are more used with larger data sets. For performance optimization
    numbers = array("i",
                    [1, 2, 3])  # the is is for the typecode. The i stands for ints. Inserting floats would return error
    numbers[0]
    return [numbers]


def sets():
    # Collection with no duplicates
    # Unordered; Doesn't support indexing
    # There is set() function
    numbers = [1, 1, 2, 3, 4]
    first = set(numbers)
    second = {1, 5}

    print(first | second)  # Union; first OR second set
    print(first & second)  # Intersection: first AND second set
    print(first - second)  # Difference of first and second set
    print(first ^ second)  # Symmetric Difference; first OR second BUT NOT first AND second set

    if 1 in first:
        print("yes")


def dictionaries():
    # Key value pairs
    # Immutable types for keys only (e.g. strings, numbers...)
    # Of any type for value
    point = {"x": 1, "y": 2}
    point = dict(x=1, y=2)
    point["x"] = 10
    point["z"] = 20
    print(point)

    if "a" in point:
        print(point["a"])

    print(point.get("a", 0))  # If there is no value of "a" then print 0 instead

    del point["x"]
    print(point)

    # Option 1 for iterating over dictionary
    for key in point:
        print(key, point[key])

    # Option 2 for iterating over dictionary
    for key, value in point.items():
        print(f"Key: {key} Value: {value}")


def dictcomprehension():
    # List comprehension
    x = list([x * 2 for x in range(5)])  # [expression for item in items]
    print(x)

    # Set comprehension
    y = {x * 2 for x in range(5)}
    print(y)

    # Dictionary comprehension
    z = {x: x * 2 for x in range(5)}  # {key: value expression for item in items
    print(z)

    w = tuple(x * 2 for x in range(5))
    print(w)  # Outputs Generator Object


from sys import getsizeof


def generatorexpressions():
    # generator objects are iterable
    # for each iteration they generate new value(s)
    # Can store lots of data with less memory
    # will not give accurate len() of values

    values = (x * 2 for x in range(100000))
    print(len(values))


def unpackingoperator():
    numbers = [1, 2, 3]
    print(numbers)
    print(*numbers)

    values1 = list(range(5))
    print(values1)
    values2 = [*range(5), *"Hello"]
    print(values2)

    first = [1, 2]
    second = [3]
    combined = [*first, "a", *second, *"Zach"]
    print(combined)

    primero = {"x": 1}
    segundo = {"x": 10, "y": 2}
    combined2 = {**primero, **segundo, "z": 88}
    print(combined2)  # x: 10  because it takes value of latest dictionary added


import math


def module6exercise(input):
    # Gets input and unzips into list
    first = [*input.lower()]
    # Get a count for each character in input and store into list
    primo = [first.count(c) for c in first]

    # zip the lists together
    # OLD CODE grandmaster = {first[x]: primo[x] for x in range(len(first))} # Could also zip it
    master = dict(zip(first, primo))
    # find largest value and store into var
    largest = max(master.values())

    # Print results based on master dictionary and largest var
    print([key for key, value in master.items() if value == largest])


from pprint import pprint


def module6exercisekey(sentence):
    char_frequency = {}

    for char in sentence.lower():
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    # turns diction pairs to tuples pairs
    char_frequency_sorted = sorted(char_frequency.items(),
                                   key=lambda kv: kv[1],
                                   reverse=True)
    print(char_frequency_sorted[0])


module6exercisekey("This is a common interview question")
module6exercise("This is a common interview question")
