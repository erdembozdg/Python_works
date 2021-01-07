import datetime
import os
import sys

today_date = datetime.datetime.now()

dir_path = os.getcwd()
if (not os.path.exists(dir_path)) and os.path.isfile(dir_path):
    sys.exit()
    
for file in os.listdir(dir_path):
    complete_path = os.path.join(dir_path, file)
    if os.path.isfile(complete_path):
        creation_date = datetime.datetime.fromtimestamp(os.path.getmtime(complete_path))
        diff_days = (today_date - creation_date).days
        print(file, diff_days)

    
