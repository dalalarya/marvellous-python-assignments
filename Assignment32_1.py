import os
import hashlib

def get_checksum(path):
    f = open(path, "rb")
    data = f.read()
    f.close()

    h = hashlib.md5(data)
    return h.hexdigest()

def show_checksum(folder):
    try:
        if os.path.exists(folder) == False:
            print("Folder not found")
            return

        files = os.listdir(folder)

        for file in files:
            full = folder + "/" + file

            if os.path.isfile(full):
                ch = get_checksum(full)
                print(file, "->", ch)

    except:
        print("Some error happened")

folder = input("Enter folder name: ")
show_checksum(folder)
