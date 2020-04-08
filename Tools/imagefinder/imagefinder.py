import os
import sys
import random
import shutil
## os.getcwd()
## os.chdir()
## os.mkdir

extensions = ['jpg','jpeg','png','gif','tif','tiff',"JPG","JPEG","PNG","GIF","TIF","TIFF"]


TOP = os.getcwd()
EXPORT = "exportedimgs"
ROOT = ""

def main():
    global ROOT
    print("Enter the root folder name")
    ROOT = input()

    if ROOT == '':
        ROOT = "root"

    if not os.path.exists(ROOT):
        print("No root folder found!")
        sys.exit()
    if os.path.exists(EXPORT):
        print("Output folder already exists!")
        sys.exit()

    os.mkdir(EXPORT)
    iterating()

def movefile(fullname, foldername,name):
    global EXPORT,TOP, ROOT
    current_backup = os.getcwd()
    exp = foldername.replace(TOP,"")
    exp = exp.replace("\\","_")  
    exp = exp[len(ROOT)+2:]
    os.chdir(EXPORT)
    if not os.path.exists(exp):
        os.mkdir(exp)
    os.chdir(exp)
    current = os.getcwd()
    #shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
    shutil.move(fullname, current + name)

    os.chdir(current_backup)


def isimage(name):
    global extensions
    image = 0
    for ext in extensions:
        if ext in name:
            image = 1
            break
    return image


def iterating():
    rootdir = os.getcwd()    
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:            
            fullname = str( os.path.join(subdir, file))
            foldername = str( os.path.join(subdir))
            name = fullname.replace(foldername,"")
            image = isimage(name)            
            if image:
                #print(fullname)
                movefile(fullname, foldername,name)

main()