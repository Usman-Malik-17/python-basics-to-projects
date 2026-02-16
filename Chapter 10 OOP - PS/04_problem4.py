class Calculator:
    def __init__(self, number):
        self.number = number

    def Square(self):
        return self.number * self.number

    def Cube(self):
        return self.number * self.number * self.number

    def SquareRoot(self):
        return self.number**1 / 2

    @staticmethod
    def greet():
        print("Hello")


C1 = Calculator(3)
C1.greet()
print(C1.Cube(), C1.SquareRoot(), C1.Square())
