import threading

def findSum(lst):
    global sum
    sum= 0
    for x in lst:
        sum += x

def findProduct(lst):
    global pro
    pro = 1
    for x in lst:
        pro *= x

lst = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=findSum, args=(lst,))
t2 = threading.Thread(target=findProduct, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Sum:", sum)
print("Product:", pro)
