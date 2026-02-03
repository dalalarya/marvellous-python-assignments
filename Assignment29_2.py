import os
fname = input("Enter file name: ")

f = open(fname, "r")
data = f.read()

if os.path.exists(fname):
    print(data)
else:
    print("File does not exist.")

f.close()
