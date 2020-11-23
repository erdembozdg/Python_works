import os
import datetime

def list_directories(path):
    for file in os.listdir(path):
        full_path = os.path.join(path, file);
        if(os.path.isdir(full_path)):
            list_directories(full_path)
        else:
            print(full_path)

list_directories(os.getcwd())
