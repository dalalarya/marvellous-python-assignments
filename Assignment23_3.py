class Numbers:
    def __init__(self, v):
        self.Value = v

    def CheckPrime(self):
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def CheckPerfect(self):
        sum= 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum = sum + i
        if sum == self.Value:
            return True
        else:
            return False

    def Factors(self):
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i)

    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum= sum + i
        return sum

n = Numbers(6)
print("Prime:", n.CheckPrime())
print("Perfect:", n.CheckPerfect())
n.Factors()
print("Sum of factors:", n.SumFactors())
