fname = input("Enter file name: ")

count = 0
f = open(fname, "r")

for line in f:
    words= line.split()
    count = count + len(words)

print("Total word count is:", count)
f.close()
