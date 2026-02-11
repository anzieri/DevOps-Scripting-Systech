#!/bin/python3
import subprocess
from pathlib import Path


#create the first directory
directoryPath= Path("dirOne")

if directoryPath.exists():
	print("DirOne already exists. Deleting any files within...")
	subprocess.run("find dirOne -mindepth 1 -delete", shell=True)
	
else:
	directoryPath.mkdir()
	print("DirOne has been created")

#create the second directory
directoryPath= Path("dirTwo")

if directoryPath.exists():
        print("DirTwo already exists. Deleting any files within...")
        subprocess.run("find dirTwo -mindepth 1 -delete", shell=True)
        
else:
        directoryPath.mkdir()
        print("DirTwo has been created")


subprocess.run("echo 'Sharon Opudo' > dirOne/Sharon.txt", shell=True)
subprocess.run("echo 'Sharon Opudo' > dirTwo/Sharon.txt", shell=True)
print("txt files created")

