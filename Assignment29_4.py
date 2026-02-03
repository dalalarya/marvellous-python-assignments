import sys

f1=open(sys.argv[1],"r")
f2=open(sys.argv[2],"r")

D1=f1.read()
D2=f2.read()

if D1 == D2:
    print("Success")
else:
    print("Failure")

f1.close()
f2.close()
