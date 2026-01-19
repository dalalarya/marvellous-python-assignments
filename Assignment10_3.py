num = int(input("Enter a number: "))

ans = 1
for i in range(1, num + 1):
    ans = ans * i

print("Factorial of entered number is:", ans)
