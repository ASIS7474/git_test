from calendar import c
import filecmp
import os
from os import *
#from re import A
#import re
import shutil
from turtle import clear
#fp = open('/home/icpluser/Downloads','r')
#os.mkdir("/home/icpluser/Downloads/folder1")
#os.mkdir("/home/icpluser/Downloads/folder2")
# for creating file
item1=["file1","file2"]
item2=["file1","file2","file3"]
path1="/home/icpluser/Downloads/folder1/"
path2= "/home/icpluser/Downloads/folder2/"

"""for i in item1:
     print('y,',i,path1)
     fle1=open(os.path.join(path1,"{}.txt".format(i)), "w")
     exit()

#files = [file for file in glob.glob("../somefolder/*")]
for file_name in item1:
    with io.open(file_name, 'r') as image_file:
        content = image_file.read()


for j in item2:
     fle2=open(os.path.join(path2,"{}.txt".format(j)), "w")   
        
def perform_all(arguments):
    switcher={
        0:
         check_file(),
        1:
         first()
        }

if __name__=="__main__":
     print("Enter 1 to check ")
     agrument = input("Enter your requirement ")
     perform_all(agrument)
"""

def check_file():
     result =  filecmp.dircmp(path1,path2)
     print("Different file found at ")
     if result.left_only:
          print('%s: %s ' % (result.left, result.left_only))
          d=result.left
          v=result.left_only
     if result.right_only:
          print('%s: %s ' % (result.right, result.right_only))
          d=result.right
          v=result.right_only
     str1=""
     b=str1.join(v)
     if result.right_only:
          shutil.copy(path.join(path2, b), path1)
     elif result.left_only:
          shutil.copy(path.join(path1, b), path2)
     print("File Copying Successfully")

check_file()

def is_same_size():
    d1_files = set(os.listdir(path1))
    d2_files = set(os.listdir(path2))
    common_files = list(d1_files & d2_files)
    if common_files:
        print(common_files)
        for filename in common_files:
            file_01 = os.stat(f'{path1}/{filename}')
            file_02 = os.stat(f'{path2}/{filename}')
            if file_01.st_size == file_02.st_size:
                print(f'The file - {filename} is identical in the directories {path1} and {path2}')
            elif file_01.st_size != file_02.st_size:
                print(f'The file - {filename} is different in the directories {path1} and'
                  f' {path2}')
                print(str(file_01.st_size)+"kb")
                print(str(file_02.st_size)+"kb")

is_same_size()


def content():  
    print("second")
    print(c)
    for i in c:
        shortname,d =  os.path.splitext(c[0])
        #for csv file we use data frame module
        if d=='.csv':
            pass
        #for text file we check readlines methods or read data row wise
        elif d=='.txt':

            pass


content()


