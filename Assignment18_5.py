
n = int(input("Enter count of numbers: "))
lst = []
for i in range(n):
    lst.append(int(input("Enter number: ")))
No = int(input("Enter number to search: "))
print("Count is:", lst.count(No))
