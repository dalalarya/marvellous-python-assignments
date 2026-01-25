from functools import reduce

num = [12, 15, 23, 17, 20]

product=reduce(lambda a,b : a * b ,num)

print(product)

