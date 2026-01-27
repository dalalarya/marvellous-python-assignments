import threading

def isprime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime(lst):
    print("Prime numbers:")
    for x in lst:
        if isprime(x):
            print(x)

def nonPrime(lst):
    print("Non-Prime numbers:")
    for x in lst:
        if not isprime(x):
            print(x)

lst = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=prime, args=(lst,), name="Prime")
t2 = threading.Thread(target=nonPrime, args=(lst,), name="NonPrime")

t1.start()
t2.start()
