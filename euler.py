def id1():
    n = int(input("Input initial value: "))
    k = int(input("Numbers to check divisibility with: "))
    calculated = n % k
    go_on = "yes"

    while n <= 1000 and go_on == "yes":
        if calculated == 0:
            print(f"Your number {n} is divisible by {k}")
            go_on = input("Go again? yes/no: ")
            if go_on == "no":
                print("Thanks for running program")
            elif go_on == "yes" or "Yes" or "YES":
                id1()

        elif calculated == True:
            print(f"Your number {n} is not divisible by {k}")
            go_on = input("Go again? yes/no: ")
            if go_on == "no":
                print("Thanks for running program")
            elif go_on == "yes" or "Yes" or "YES":
                id1()


id1()
