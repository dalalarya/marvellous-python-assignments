num = (input("Enter a number: "))

rev=""

for i in num:
    rev=i+rev

if num==rev:
    print("palindrome")
else:
    print("Not palindrome")
    
