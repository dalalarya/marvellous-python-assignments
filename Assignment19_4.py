from functools import reduce

lst = [5,2,3,4,3,4,1,2,8,10]

fil = list(filter(lambda x: x%2==0, lst))
ma = list(map(lambda x: x*x, fil))
red = reduce(lambda a,b: a+b, ma)

print("Filter:", fil)
print("Map:", ma)
print("Reduce:", red)
