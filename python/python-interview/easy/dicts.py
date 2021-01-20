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


dict1 = {1: 1, 2: 9, 3: 4}
sorted_values = sorted(dict1.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break

print(sorted_dict)

dict1 = {1: 1, 2: 9, 3: 4}
sorted_dict = {}
sorted_keys = sorted(dict1, key=dict1.get)  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = dict1[w]

print(sorted_dict) # {1: 1, 3: 4, 2: 9}