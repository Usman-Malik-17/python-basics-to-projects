class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


P1 = Programmer("Usman", 1200000, 1234)

print(P1.name, P1.salary, P1.pin)
P2 = Programmer("Adnan", 1200000, 54321)

print(P2.name, P2.salary, P2.pin)
