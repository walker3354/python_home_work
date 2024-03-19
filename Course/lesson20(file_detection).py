import os
path = "E:\\program\\python\\Course\\test_folder"

if os.path.exists(path):
    print('find the previous save folder')
    if os.path.isfile(path):
        print('this is a file')
    elif os.path.isdir(path):
        print('this is a folder')
else:
    print("can't find anything")
