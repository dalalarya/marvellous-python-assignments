import os
import hashlib
import time

def get_checksum(path):
    f = open(path, "rb")
    data = f.read()
    f.close()
    return hashlib.md5(data).hexdigest()

def delete_with_time(folder):
    start = time.time()

    try:
        seen = {}

        for file in os.listdir(folder):
            full = folder + "/" + file
            if os.path.isfile(full):
                ch = get_checksum(full)

                if ch in seen:
                    os.remove(full)
                    print(file, "deleted")
                else:
                    seen[ch] = file

    except:
        print("Error occurred")

    end = time.time()
    print("Time taken:", end - start)

folder = input("Enter folder name: ")
delete_with_time(folder)
