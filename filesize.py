import os
import sys
from os import path

argvs = sys.argv  #get commandline list
argc = len(argvs) #get commandline count


if(argc < 2):  
	mydir = os.getcwd()
else:          
	mydir = argvs[1]

files = os.listdir(mydir) #get filenames in mydir

for file in files:
	print path.getsize(file),'byte'
