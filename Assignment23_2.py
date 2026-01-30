class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Name:", self.Name)
        print("Balance:", self.Amount)

    def Deposit(self, x):
        self.Amount = self.Amount + x

    def Withdraw(self, x):
        self.Amount = self.Amount - x

    def CalculateInterest(self):
        return (self.Amount * BankAccount.ROI) / 100

b1 = BankAccount("Arya", 1000)
b1.Display()

b1.Deposit(500)
b1.Withdraw(200)

print("Interest:", b1.CalculateInterest())
b1.Display()
