f1 = input("Enter old file name: ")
f2 = input("Enter new file name: ")

oldfile= open(f1, "r")
data = oldfile.read()

newfile = open(f2, "w")
newfile.write(data)

oldfile.close()
newfile.close()
