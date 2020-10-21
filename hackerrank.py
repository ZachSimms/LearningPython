
# Not Complete
def compareTriplets(a, b):
    # first = (a[0],a[1],a[2])
    # second = (a[0],a[1],a[2])
    x = 0
    y = 0

    for m in a[0]:
        for n in b[0]:
            if m > b:
                x += 1
            elif a[m] < b[n]:
                y += 1
            else:
                break

    print("A score is: {}", x)
    print("B score is: {}", y)

compareTriplets([1,2,3], [3,2,1])