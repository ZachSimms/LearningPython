

# Create a function (or write a script in Shell)
# that takes an integer as an argument and returns
# "Even" for even numbers or "Odd" for odd numbers.
def even_or_oddv1(number):
    # This was my solution
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def even_or_oddv2(number):
    # Peer solution
    return 'Odd' if number % 2 else 'Even'

def even_or_oddv3(number):
    # Peer solution
    return ["Even", "Odd"][number % 2]


# The goal of this exercise is to convert a string to
# a new string where each character in the new string
# is "(" if that character appears only once in the original
# string, or ")" if that character appears more than
# once in the original string. Ignore capitalization
# when determining if a character is a duplicate.
from collections import Counter
def duplicate_encodev1(word):
    # My solution
    master = []
    grandmaster = []
    god = ""

    # Take word and turn into list called master. Also ensures all letters are lowercase
    for x in enumerate(word.lower()):
        master.append(x[1])

    # Takes list(master) and determines count for each item and stores the counts in another list
    for x in master:
        grandmaster.append(master.count(x))

    # Takes list of counts and determines if ( or ) will be
    # appended onto the string god based on count
    for x in grandmaster:
        if x == 1:
            god += "("
        else:
            god += ")"

    print(god)

def duplicate_encodev2(word):
    # Peer Solution
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

def duplicate_encodev3(word):
    word = word.lower()
    counter = Counter(word)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)
