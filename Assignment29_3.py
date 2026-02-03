import sys

f1 = open(sys.argv[1], "r")
data = f1.read()

f2 = open("Demo.txt", "w")
f2.write(data)

f1.close()
f2.close()

print("Content copied successfully.")
