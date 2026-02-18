import os
import shutil

def write_log(msg):
    f = open("log.txt", "a")
    f.write(msg + "\n")
    f.close()

def copy_ext(src, dest, ext):
    try:
        if os.path.exists(dest) == False:
            os.mkdir(dest)

        files = os.listdir(src)

        for file in files:
            if file.endswith(ext):
                shutil.copy(src + "/" + file, dest)
                write_log(file + " copied")

    except:
        write_log("Error occurred")

src = input("Enter source folder: ")
dest = input("Enter destination folder: ")
ext = input("Enter extension: ")

copy_ext(src, dest, ext)
