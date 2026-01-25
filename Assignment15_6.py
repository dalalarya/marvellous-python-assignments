from functools import reduce

num=[10,101,273,104,235]

min=reduce(lambda a,b: b if a > b else a,num )
print(min)