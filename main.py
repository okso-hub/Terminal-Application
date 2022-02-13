from fileinput import filename
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


def delete_file(file_name):
    os.remove(file_name)


def delete_directory(dir_name):
    os.rmdir(dir_name)


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
                try:
                    change_directory(f"{second_command} {commands[2]}")
                except:
                    change_directory(second_command)
        
        elif first_command == "pwd":
            print(actual_path)

        elif first_command == "mkdir":
            create_directory(second_command)
        
        elif first_command == "ls":
            list_content(actual_path)
        
        elif first_command == "rm":
            delete_file(second_command)
        
        elif first_command == "rmdir":
            delete_directory(second_command)
        
        elif first_command == "open":
            os.system(f"open {second_command}")

        elif first_command == "clear":
            clear()
        
        elif first_command == "python":
            exec(open(f"{second_command}").read())
        
        elif first_command == "quit":
            break
        
        else:
            print(f"Command '{first_command}' not found.")


if __name__ == "__main__":
    main()
