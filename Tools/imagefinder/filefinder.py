import os
import sys
import random
import shutil
## os.getcwd()
## os.chdir()
## os.mkdir

#extensions = ['jpg','jpeg','png','gif','tif','tiff',"JPG","JPEG","PNG","GIF","TIF","TIFF"]
extensions = ['docx','doc','xls','xlsx','xlm','xlsm','pdf','csv','jpg','jpeg','png','ppt','pptx',
                'DOCX','DOC','XLS','XLSX','XLM','XLSM','PDF','CSV','JPG','JPEG','PNG','PPT','PPTX']


PARENT_DIR = os.getcwd()
EXPORTFOLDER = "exportedfiles"
ROOT = ""

def main():
    global ROOT
    print("Enter the root folder name")
    ROOT =  "/home/alexis/Documents/Repositorios/programas-python/Tools/imagefinder/root/f2N0"    
    if ROOT == '':
        ROOT = "root"

    if not os.path.exists(ROOT):
        print("No root folder found!")
        sys.exit()
    if os.path.exists(EXPORTFOLDER):
        print("Output folder already exists!")
        sys.exit()

    os.mkdir(EXPORTFOLDER)
    iterating(ROOT)

def movefile(fullname, foldername,name):
    global EXPORTFOLDER,PARENT_DIR, ROOT
    current_backup = os.getcwd()
    exp = foldername.replace(PARENT_DIR,"") # new relative folder
    if os.name == 'posix':
        exp = exp.replace("/","_")      
    else:
        exp = exp.replace("\\","_")  
    exp = exp[len(ROOT)+2:]
    os.chdir(EXPORTFOLDER)
    if not os.path.exists(exp):
        os.mkdir(exp)
    os.chdir(exp)
    current = os.getcwd()
    #shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
    shutil.copy(fullname, current + name)

    os.chdir(current_backup)


def check_extension(name):
    global extensions
    isType = 0
    for ext in extensions:
        if ext in name.lower():
            isType = 1
            break
    return isType


def iterating(rootdir):    
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:            
            fullname = str( os.path.join(subdir, file))
            foldername = str( os.path.join(subdir))
            name = fullname.replace(foldername,"")
            isTypeSearched = check_extension(name)            
            if isTypeSearched:
                print(fullname)
                #movefile(fullname, foldername,name)

main()