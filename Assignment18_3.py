
n = int(input("Enter Number of elements: "))
lst = []

for i in range(n):
    num = int(input("Enter a number: "))
    lst.append(num)

print("Minimum number:",min(lst))
