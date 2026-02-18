import os

def write_log(msg):
    f = open("log.txt", "a")
    f.write(msg + "\n")
    f.close()

def search_files(folder, ext):
    try:
        if os.path.exists(folder) == False:
            write_log("Folder not found")
            return

        for file in os.listdir(folder):
            if file.endswith(ext):
                write_log(file)

    except:
        write_log("Error occurred")

folder = input("Enter folder name: ")
extension = input("Enter extension: ")

search_files(folder, extension)
