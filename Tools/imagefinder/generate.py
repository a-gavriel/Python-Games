import os
import random
import shutil
## os.getcwd()
## os.chdir()
## os.mkdir


TOP = os.getcwd()
ROOT = "root"
EXPORT = "exportedimgs"
counter = 0
# deletes root folder and subfolders with files
def generate_root():
  global ROOT, EXPORT
  if os.path.exists(ROOT):
    shutil.rmtree(ROOT)
  if os.path.exists(EXPORT):
    shutil.rmtree(EXPORT)
  os.mkdir(ROOT)
  
# generates the empty files with the names from the list
def generate_files():
  global counter
  list_3 = ["a.jpg","a.jpeg","a.png"]
  for i in list_3:
    f = open(str(counter)+i,'a+')
    counter+=1
    f.close()

# generates the folders and inserts the files inside, it can concatenate folders inside folders until reachigna depth of N = 3
def generate_folders(N=0):
  list_1 = ["f1","f2"]
  if N < 3:
    for i in list_1:
      os.mkdir(i+"N"+str(N))
      os.chdir(i+"N"+str(N))
      generate_files()
      new_ = random.randint(1,3)
      if new_ != 2:
        generate_folders(N+1)
      os.chdir("..")
		

def main():
  global ROOT
  generate_root()
  os.chdir(ROOT)
  generate_folders()


main()