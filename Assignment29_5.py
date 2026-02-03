import sys

f = open(sys.argv[1], "r")
data = f.read()

word = sys.argv[2]
count = data.count(word)

print("Frequency is:", count)

f.close()
