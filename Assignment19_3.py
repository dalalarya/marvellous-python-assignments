
from functools import reduce

lst = [4,34,36,76,68,24,89,23,86,90,45,70]

fil = list(filter(lambda x: x>=70 and x<=90, lst))
ma = list(map(lambda x: x+10, fil))
red = reduce(lambda a,b: a*b, ma)

print("Filter:", fil)
print("Map:", ma)
print("Reduce:", red)
