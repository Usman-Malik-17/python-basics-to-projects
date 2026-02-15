def greatestOfThreeNumbers(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(f"Greatest of three numbers is: {greatestOfThreeNumbers(10, 10, 5)}")
