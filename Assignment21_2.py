
import threading

lst = list(map(int, input("Enter numbers: ").split()))

def findMax():
    print("Maximum:", max(lst))

def findMin():
    print("Minimum:", min(lst))

t1 = threading.Thread(target=findMax)
t2 = threading.Thread(target=findMin)

t1.start()
t2.start()

t1.join()
t2.join()

