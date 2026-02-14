a = int(input("Enter a number: "))
star = 1

for i in range(1, a + 1):

    for s in range(a - i):
        print(" ", end="")

    for j in range(star):
        print("*", end="")

    star += 2
    print()
