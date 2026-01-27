import threading

def evenfactor(n):
    sum=0
    print("Even factors:")
    for i in range(1,n+1):
        if n%1==0 and i%2==0:
            print(i)
            sum+=i
    print("Sum of Even:",sum)


def oddFactor(n):
    sum = 0
    print("Odd factors:")
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 1:
            print(i)
            sum+= i
    print("Sum of odd:", sum)

num = int(input("Enter number: "))

t1 = threading.Thread(target=evenfactor, args=(num,))
t2 = threading.Thread(target=oddFactor, args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")



