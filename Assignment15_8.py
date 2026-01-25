num = [10, 14, 20, 27, 60]
div = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, num))
print(div)
