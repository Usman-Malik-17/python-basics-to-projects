a = int(input("Enter a number: "))
space = a - 1
star = 1

for i in range(1, a + 1):
    print(" " * space, end="")
    space = space - 1
    print("*" * star, end="")
    star = star + 2
    print(" ")
