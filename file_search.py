import os, time

# os , time should be pre installed

start_path = "/storage/emulated/0/"  # input your preset path examples:

liste = []
# android = /storage/emulated/0/
# linux = /home/user-name/
# windows = C:\User\user-name\

def search_file(search, path):
    start = time.time()  # starts the timer
    n = 0
    if os.path.isdir(path) or os.path.isfile(path):  # checks if the path from the user does exist

        for root, dirs, files in os.walk(path):
            n += 1
            if search in files:
                print("siblings: ")  # files that are on the same path and are folders
                for file in files:
                    if file == search:
                        print('\033[32m', file + '\033[37m', "|", end="")  # prints the search file in a different color
                    else:
                        print(file + "|", end="")

                end = time.time()  # ends the timer
                clock = str(end - start)

                if start_path not in root:  # adds start_path to the root to show it completely
                    root = start_path + root

                clock = float(clock)
                clock = round(clock, 2)

                print('\n', '-' * 35)
                print("file was located in")
                print("path: ", root)
                print("it took ", clock, "s")
                print("tries: ", n)
                if input("do you want to continue searching? [Y/N]").lower() == "y":
                    liste.insert(0, "path: " + root + "\n" + "it took " + str(clock) + "s" + "\n" + "tryes: " + str(n) + "\n")
                else:
                    print("\n", "-" * 35)
                    for listen in liste:
                        print(listen)
                    return None
                return None  # else it would print the last line

        print(f"could not find file ({search})")
        return None
    else:
        print(f"'{path}' does not exist")
        return None


def search_folder(search, path):
    start = time.time()  # starts the timer
    n = 0
    if os.path.isdir(path) or os.path.isfile(path):  # checks if the path from the user does exist

        for root, dirs, files in os.walk(path):  # goes through the path
            n += 1
            if search in files:
                print("siblings: ")  # files that are on the same path and are folders
                for file in files:
                    if file == search:
                        print('\033[32m', file + '\033[37m', "|", end="")  # prints the search file in a different color
                    else:
                        print(file + "|", end="")

                end = time.time()  # ends the timer
                clock = str(end - start)

                if start_path not in root:  # adds start_path to the root to show it completely
                    root = start_path + root

                clock = float(clock)
                clock = round(clock, 2)

                print('\n', '-' * 35)
                print("file was located in")
                print("path: ", root)
                print("it took ", clock, "s")
                print("tries: ", n)
                if input("do you want to continue searching? [Y/N]").lower() == "y":
                    liste.insert(0, "path: " + root + "\n" + "it took " + str(clock) + "s" + "\n" + "tryes: " + str(n) + "\n")
                else:
                    print("\n", "-" * 35)
                    for listen in liste:
                        print(listen)
                    return None
                return None  # else it would print the last line

        print(f"could not find file ({search})")
        return None
    else:
        print(f"{path} does not exist")
        return None


def info():
    inp_info = input("input a dir[1] or file[2]\n")

    if inp_info == "1":
        file_name = input("input the name of the folder\n")
        path_i = input(f"input a path else press enter\n`{start_path}` +") or start_path

        search_folder(file_name, path_i)

    elif inp_info == "2":
        file_name = input("input the name of the file\n")
        path_i = input(f"input a path else press enter\n`{start_path}` +") or start_path

        search_file(file_name, path_i)
    else:
        print("try again")
        return None


while True:
    info()
    print("-" * 33)