class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0
        self.area = 0
        self.circum = 0

    def Accept(self):
        self.radius = float(input("Enter radius: "))

    def Area(self):
        self.area = self.radius * self.radius * Circle.PI

    def Circumference(self):
        self.circum = 2 * Circle.PI * self.radius

    def Display(self):
        print("Radius:", self.radius)
        print("Area:", self.area)
        print("Circumference:", self.circum)

c1 = Circle()
c1.Accept()
c1.Area()
c1.Circumference()
c1.Display()
