
from functools import reduce

lst = [2,70,11,10,17,23,31,77]

def prime(n):
    if n<2: 
        return False
    for i in range(2,n):
        if n%i==0: return False
    return True

fil = list(filter(prime, lst))
ma = list(map(lambda x: x*2, fil))
red = reduce(lambda a,b: a if a>b else b, ma)

print("Filter:", fil)
print("Map:", ma)
print("Reduce:", red)
