import os
from getpass import getuser


clear = lambda: os.system("clear") if os.name == "posix" else os.system("cls")


def create_file(file_name): # touch
    with open(file_name, "w") as f:
        f.write("")


def change_directory(path): # cd [filename]
    os.chdir(path)


def create_directory(dir_name):
    os.mkdir(dir_name)


def step_back(): #  cd ..
    os.chdir("..")


def list_content(actualpath):
    for i in os.listdir(actualpath):
        print(i)


def main():
    username = getuser()
    os.chdir(f"/users/{username}")
    while True:
        actual_path = os.path.abspath(os.getcwd())
        print(f"{actual_path}/", end=" ")
        entry = str(input(""))

        commands = entry.split(" ")
        first_command = commands[0]
        try:
            second_command = commands[1]
        except:
            second_command = ""

        if first_command == "touch":
            create_file(second_command)

        elif first_command == "cd":
            if second_command == "..":
                step_back()
            elif second_command == "":
                os.chdir("/users/")
            else:
                change_directory(second_command)
        
        elif first_command == "pwd":
            print(actual_path)

        elif first_command == "mkdir":
            create_directory(second_command)
        
        elif first_command == "ls":
            list_content(actual_path)

        elif first_command == "clear":
            clear()
        
        else:
            break


if __name__ == "__main__":
    main()
