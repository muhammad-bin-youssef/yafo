
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
import re

# golbal variable
folders = []

#constant
start = '/home/mhy/Documents/py'
# --------------------------------------Functions--------------------------------------

def search_system():
    for path, subfolder, file  in os.walk(start):
        folders.append(folder_maker(path, file, subfolder))
    
def is_yafoFile(fileName): 
    if type(fileName) == 'list':
        #
        if 'yafo' in fileName:
            return True
        return False


def change_name(fileName, *path):
    re_obj = re.compile(r'[\d\w\-\\\/\.]+?yafo')                                  
    name = re_obj.search(fileName)
    # fileName[: name.span()[1]-4] is the destination
    # fileName[name.span([1]:)] the original file name
    #move_file()
    print(type(path))
def move_file(fileName, destination):
    '''This func take two arg. (fileName, destination)'''
    shutil.move(fileName, destination)    

    
def folder_maker(path, file, subfolder):
    """Take three arguments (path, file, subfolder) return dict""" 
    folders = {
        "path" : path,
        "dirName" : os.path.dirname(path),
        "baseName" : os.path.basename(path),
        "files" : file,
        "subFolders" : subfolder,
        "date" : "", 
        }
    return folders

if __name__ == '__main__':
    search_system() 
    change_name('documentation_falk-ajkf.akldyafoyafo_my_project.txt')