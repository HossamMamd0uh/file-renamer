
import os

#Renames the multiple file within the same directory with appending number


#Replace os.getcwd with file path

path =  os.getcwd()
files = os.listdir(path)
i = 1

for file in files:
    filename, file_extension = os.path.splitext(file)
    
    #Replace Project with the name you want
    os.rename(os.path.join(path, file), os.path.join(path, "Project" + str(i) + file_extension))
    i = i+1
