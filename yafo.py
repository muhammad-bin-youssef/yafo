
# --------------------------------------NAME--------------------------------------

# yafo -> Yet Another File Organizer 

# --------------------------------------Why did I make it--------------------------------------

# This program is Slow file manger 
# Remeber sometimes when you downoads images system automaticle download it into 'Downlaods' but you have seprate folders like one for 
# for you application web but onther path for your wallpapers or anothr one for your familiy 

# --------------------------------------How it work--------------------------------------

# This program choose what files to orginize and what to ignore depending on the fiel name
# exampel: Documentationyafo-my_project.txt
# 'Documentaion' is the destination
# 'yafo' is the trigger
# '-' is for syntax and is not nececrey
# 'my_project' is the file name 
# '.txt' is the extension
# 
# '' is the destination(is the path where your file is going to go)
# 'yafo' end it with yafo and you may add "-" after yafo for syntax the program automatically will 
# delet it

# --------------------------------------What argument you could add--------------------------------------

#

# Legal charecters uppercase (A–Z), lowercase (a–z) letters, digits (0–9), hyphens (-), 
# underscores (_), and a single period (.)

import os 
import time
import shutil

# golbal variable
folders = []

#constant
start = '/home/mhy/Documents'
# --------------------------------------Functions--------------------------------------

def make_map():
    def folder_maker(path, file, subfolder):
        folders = {
            "path" : path,
            "dirName" : os.path.dirname(path),
            "baseName" : os.path.basename(path),
            "files" : file,
            "subFolders" : subfolder,
            "date" : "", 
            }
        return folders
    for path, subfolder, file  in os.walk(start):
        folders.append(folder_maker(path, file, subfolder))
    

def is_yafoFile(fileName, j, i): 
    if type(fileName) == 'list':
        if 'yafo' in fileName:
            print("list")
            move_file(os.path.join(folders[i]['path'],folders[i]['files'][j]))
    if type(fileName) == 'str':
        print("file")
        move_file(os.path.join(folders[i]['path'],folders[i]['files'][j]))
        


def move_file(filePath): # file path + old file name 
    pfile = os.path.basename(filePath)
    for i in range(len(folders)):
        if folders[i]['baseName'] == pfile[:pfile.index('yafo')]:
            newFIle = pfile[(pfile.index('yafo') + 4):]
            shutil.move(filePath, os.path.join(folders[i]['path'], newFIle))
            break

def machine():
    for i in range(len(folders)):
        for j in range(len(folders[i]['files'])):
            is_yafoFile(folders[i]['files'][j],j ,i)




if __name__ == '__main__':
    make_map() 
    machine()


