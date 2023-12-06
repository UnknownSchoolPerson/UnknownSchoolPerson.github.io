# import OS module
import os
 
# Get the list of all files and directories
path = "C://Users//{USER}//source//repos//MB2-Map//MB2 Map//Towns - Copy"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)

for file in dir_list:
    f = open(path + "//" + file, "r")
    print('"', file.split('.')[0], '"', ',',f.read(), end="", sep="")
    f.close()
