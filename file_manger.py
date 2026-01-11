import os 

# golbal variable
folders = []

def 

def folder_maker(folder, file, subdolder):
    """Take three arguments (folder, file, subfolder) return dict
    # for x in range(3):    
#     print(folders[x]["folder"])    
#     print(folders[x]["dirName"])
#     print(folders[x]["baseName"])
#     print(folders[x]["files"])
#     print(folders[x]["subFolders"])
#     print()""" 
    
    folders = {
        "folder" : folder,
        "dirName" : os.path.dirname(folder),
        "baseName" : os.path.basename(folder),
        "files" : file,
        "subFolders" : subdolder 
        }
    return folders

for folder, subfolder, file  in os.walk(r'/home/mhy/Documents/py'):
    folders.append(folder_maker(folder, file, subfolder)
)

