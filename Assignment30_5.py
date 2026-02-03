fname = input("Enter file name: ")
word = input("Enter word to find: ")

f = open(fname, "r")
data = f.read()

if word in data:
    print("Word found")
else:
    print("Word not found")

f.close()
