import threading

def evenList(lst):
    sum = 0
    for x in lst:
        if x % 2 == 0:
            print("Even number:", x)
            sum+= x
    print("Even sum is:", sum)

def oddList(lst):
    sum = 0
    for x in lst:
        if x % 2 == 1:
            print("Odd number:", x)
            sum += x
    print("Odd sum is:", sum)

lst = [1,2,3,4,5,6,7,8,9]

t1 = threading.Thread(target=evenList, args=(lst,))
t2 = threading.Thread(target=oddList, args=(lst,))

t1.start()
t2.start()
