import os

def write_log(msg):
    f = open("log.txt", "a")
    f.write(msg + "\n")
    f.close()

def rename_files(folder, old_extension, new_extension):
    try:
        files = os.listdir(folder)

        for file in files:
            if file.endswith(old_extension):
                old_name = folder + "/" + file
                new_name = folder + "/" + file.replace(old_extension, new_extension)
                os.rename(old_name, new_name)
                write_log(file +"renamed")

    except:
        write_log("Error occurred")

folder = input("Enter folder name: ")
old_extension = input("Enter old extension: ")
new_extension = input("Enter new extension: ")

rename_files(folder, old_extension, new_extension)
