import os
import hashlib

def get_checksum(path):
    f = open(path, "rb")
    data = f.read()
    f.close()
    return hashlib.md5(data).hexdigest()

def find_duplicates(folder):
    try:
        seen = {}

        for file in os.listdir(folder):
            full = folder + "/" + file
            if os.path.isfile(full):
                ch = get_checksum(full)

                if ch in seen:
                    print("Duplicate:", file)
                else:
                    seen[ch] = file

    except:
        print("Error occurred")

folder = input("Enter folder name: ")
find_duplicates(folder)
