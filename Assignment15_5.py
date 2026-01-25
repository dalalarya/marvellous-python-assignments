from functools import reduce

num=[10,101,273,104,235]

max=reduce(lambda a,b: a if a > b else b,num )
print(max)