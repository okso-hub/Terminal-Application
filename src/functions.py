from fileinput import filename
import os
from getpass import getuser
from pathlib import Path
import shutil


clear = lambda: os.system("clear") if os.name == "posix" else os.system("cls")


def create_file(file_name): # touch
    with open(file_name, "w") as f:
        f.write("")


def change_directory(path): # cd [filename]
    os.chdir(path)


def create_directory(dir_name):
    os.mkdir(dir_name)


def step_back(): # cd ..
    os.chdir("..")


def list_content(actualpath):
    for i in os.listdir(actualpath):
        print(i)


def delete_file(file_name):
    os.remove(file_name)


def delete_directory(dir_name):
    os.rmdir(dir_name)


def move_file(file_name, destination):
    shutil.move(file_name, destination)
