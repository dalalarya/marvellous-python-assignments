import threading

num = 0
lock = threading.Lock()

def inc():
    global num
    for i in range(3):
        lock.acquire()
        num = num + 1
        print("Count:", num)
        lock.release()

t1 = threading.Thread(target=inc)
t2 = threading.Thread(target=inc)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Value:", num)
