import os
from os import path
import shutil
import glob

s = str(os.getcwd())
s += '/*.java'
create_dir = "sample"

if(path.isdir(create_dir)):  #already exists directory
	shutil.rmtree(create_dir)
os.mkdir(create_dir)  #create directory
for file in glob.glob(s):
	shutil.copy(file,create_dir)



