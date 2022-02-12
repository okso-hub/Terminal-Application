import os

def create_file(file_name):
    with open(file_name, "w") as f:
        f.write("")


def change_directory(path):
    os.chdir(path)


def step_back():
    os.chdir("..")


def main():
    os.chdir("/users/")
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


if __name__ == "__main__":
    main()
