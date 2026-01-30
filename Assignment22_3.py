
class Arithematic:
    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self):
        self.value1=int(input("Enter first number:"))
        self.value2=int(input("Enter second number:"))

    def Add(self):
        print("Addition =", self.value1 + self.value2)

    def Sub(self):
        print("Subtraction =", self.value1 - self.value2)

    def Mul(self):
        print("Multiplication =", self.value1 * self.value2)

    def Div(self):
        print("Division =", self.value1 / self.value2)

a1 = Arithematic()
a1.Accept()
a1.Add()
a1.Sub()
a1.Mul()
a1.Div()
