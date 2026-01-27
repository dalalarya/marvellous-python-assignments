import threading

def in1():
    for i in range(1, 51):
        print("Thread1:", i)

def inrev():
    for i in range(50, 0, -1):
        print("Thread2:", i)

t1 = threading.Thread(target=in1)
t2 = threading.Thread(target=inrev)

t1.start()
t1.join()   

t2.start()
t2.join()

