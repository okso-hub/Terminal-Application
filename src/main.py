from functions import *


def main():
    username = getuser()
    os.chdir(f"/users/{username}")
    while True:
        current_path = os.path.abspath(os.getcwd())
        print(f"{current_path}/", end=" ")
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
            print(current_path)

        elif first_command == "mkdir":
            create_directory(second_command)
        
        elif first_command == "ls":
            list_content(current_path)
        
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
        
        elif first_command == "mv":
            move_file(second_command, commands[2])
        
        elif first_command == "quit":
            break
        
        else:
            print(f"Command '{first_command}' not found.")


if __name__ == "__main__":
    main()
