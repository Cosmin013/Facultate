import sys
import os
from zipfile import ZipFile
def search_by_content(target, to_search):
    result_list = []

    if not os.path.exists(target):
        return result_list

    if os.path.isfile(target):
        file = open(target, "r")
        for line in file:
            if to_search in line:
                result_list.append(file.name)
                return result_list

    if os.path.isdir(target):
        for (root, directories, files) in os.walk(target):
            for fileName in files:
                file = open(os.path.join(root, fileName), "r")
                for line in file:
                    if to_search in line:
                        result_list.append(fileName)
                        break
        return result_list

    return result_list

print(search_by_content("test.txt", "Text"))

def get_file_info(path):
    result = dict()
    absPath = os.path.abspath(path)
    result.update({"full_path" : absPath})

    size = os.path.getsize(path)
    result.update({"file_path" : size})

    extension = os.path.splitext(path)
    result.update({"file_extension" : extension[1]})

    permission = list()
    permission.append(os.access(path, os.R_OK))
    permission.append(os.access(path, os.W_OK))

    result.update({"file_perms" : permission})

    return result


def functie3(fileName):
    try:
        file = open(fileName, "w")
        env_var = os.environ
        file.write(dict(env_var))
    except Exception as e:
        print(e)

def functie4(dir):
    for f in os.listdir(dir):
        path = os.path.join(dir, f)
        if os.path.isfile(path):
            print(os.path.abspath(path), "FILE")
        elif os.path.isdir(path):
            print(os.path.abspath(path), "DIR")
            functie4(path)
        else:
            print(os.path.abspath(path), "unk")

# def functie5(source, dir, buf_size):

def functie6(dirpath):
    result = dict()

    full_path = os.path.abspath(dirpath)
    result.update({"full_path: ": full_path})

    total_size = 0
    file_list = list()
    dir_list = list()

    for (root, directories, files) in os.walk(dirpath):
        for file in files:
            fullpath = os.path.join(root, file)
            total_size += os.path.getsize(fullpath)
            file_list.append(os.path.relpath(fullpath, dirpath))

        for dirs in directories:
            fullpath = os.path.join(root, dirs)
            dir_list.append(os.path.abspath(fullpath))


    result.update({"files:": file_list})
    result.update({"directories: " : dir_list})
    return result

def functie7(container_path):
    with ZipFile(container_path, 'r') as zip:
        zip.printdir()
        zip.extractall()

functie7('.\\test.zip')

# print(functie6('.'))

# functie4('.')


# functie("test.txt")

# print(get_file_info("test.txt"))

# if __name__ == "__main__":
    # prints current path
    # print("Path:", sys.argv[0])

    # suma = 0
    # try:
    #     for val in sys.argv[1:]:
    #         suma += int(val)
    #     print("Suma = ", suma)
    # except:
    #     print("Invalid parameters")

    # prints what is in dir
    # print(os.listdir("."))

    # print(os.path.isdir("C:\\Windows"))
    # print(os.path.isfile("C:\\Windows"))
    # print(os.path.isfile("C:\\Windows\\csup.txt"))
    # print(os.path.isdir("C:\\Windows\\csup.txt"))
    # print(os.path.splitext("C:\\Windows\\csup.txt"))


    # listing folder contents recursively
    # for(root, directories, files) in os.walk("."):
    #     for fileName in files:
    #         full_fileName = os.path.join(root, fileName)
    #         print(fileName)
    #         print(root)
    #         print(full_fileName)

    # print("pula", "pizda", "alteva", sep="condom")
    # print("pula", "pizda", "alteva", sep="condom", flush = True)

    # for line in open("lab9.py"):
    #     print(line.rstrip())

   # open("test.txt", "wt").write("Text fasga")



