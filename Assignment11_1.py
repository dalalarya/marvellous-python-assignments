num = int(input("Enter a number: "))

div = 0

for i in range(1, num + 1):
    if num % i == 0:
        div = div + 1

if div == 2:
    print("The number entered is a Prime Number")
else:
    print("The number entered is not Prime number")
