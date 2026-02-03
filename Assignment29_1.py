import os

fname = input("Enter file name: ")

if os.path.exists(fname):
    print("File exists.")
else:
    print("File does not exist.")
