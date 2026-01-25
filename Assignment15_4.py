from functools import reduce

num=[1,2,3,4,5,6,7,8,9,10]

sum=reduce(lambda a,b: a + b,num )
print(sum)