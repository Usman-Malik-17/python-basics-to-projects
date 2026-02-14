a = int(input("Enter a number: "))

if a <= 1:
    print(f"{a} is not a prime number")
else:
    b = a - 1
    while b > 1:
        if a % b == 0:
            print(f"{a} is not a prime number")
            break
        b -= 1
    else:
        print(f"{a} is a prime number")
