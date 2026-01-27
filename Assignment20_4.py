import threading

def count_small(text):
    small = 0
    for ch in text:
        if ch >= 'a' and ch <= 'z':
            small += 1
    print("Small letters:", small)
    print("Thread ID:", threading.get_ident())
    print("Thread name is:", threading.current_thread().name)

def count_capital(text):
    cap = 0
    for ch in text:
        if ch >= 'A' and ch <= 'Z':
            cap += 1
    print("Capital letters:", cap)
    print("Thread ID:", threading.get_ident())
    print("Thread name is:", threading.current_thread().name)

def count_digits(text):
    d = 0
    for ch in text:
        if ch >= '0' and ch <= '9':
            d += 1
    print("Digits:", d)
    print("Thread ID:", threading.get_ident())
    print("Thread name is:", threading.current_thread().name)

s = input("Enter a string: ")

t1 = threading.Thread(target=count_small, args=(s,), name="Small")
t2 = threading.Thread(target=count_capital, args=(s,), name="Capital")
t3 = threading.Thread(target=count_digits, args=(s,), name="Digits")

t1.start()
t2.start()
t3.start()
