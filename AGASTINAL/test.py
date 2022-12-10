
import os

def change_dir(path):
    os.chdir(path)
    print(os.getcwd())
