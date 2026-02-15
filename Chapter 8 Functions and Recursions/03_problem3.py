def printStar(n):
    if n == 0:
        return
    elif n > 0:
        print(n * "*")
        printStar(n - 1)


printStar(10)
