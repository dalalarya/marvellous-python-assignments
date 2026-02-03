fname = input("Enter file name: ")

f = open(fname, "r")
TotalLines = f.readlines()

print("Total lines are:", len(TotalLines))
f.close()
