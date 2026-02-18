import os
import shutil

def write_log(msg):
    f = open("log.txt", "a")
    f.write(msg + "\n")
    f.close()

def copy_all(source, destination):
    try:
        if os.path.exists(destination) == False:
            os.mkdir(destination)

        files = os.listdir(source)

        for file in files:
            shutil.copy(src + "/" + file, destination)
            write_log(file + " copied")

    except:
        write_log("Error occurred")

source = input("Enter source folder: ")
destination = input("Enter destination folder: ")

copy_all(source, destination)
