import shutil
import os
import time

path = input("enter file path: ")
exists = os.path.exists(path)
time2 = time.time()
if(exists == True):
    days = int(input("enter the file date creation range that needs to be deleted: "))
    seconds = days * 86400
    stTime = os.stat(path)
    dir = os.listdir(path)
    print(dir)
    print(time2)
    print(stTime)
    fileCDate = time2 - stTime[9]
    if(fileCDate > seconds):
        print("The above files are older than", days)
        confirmation = input("are you sure you want to delete them y/n ? ")
        if(confirmation == "y"):
            os.remove(path)
            shutil.rmtree(path)
        if(confirmation == "n"):
            print("process cancelled")
    
    if(fileCDate < seconds):
        print("there are no files which have been created before", days, "days")
    
if(exists == False):
    print("The path which you have enterred does not exist")
    
