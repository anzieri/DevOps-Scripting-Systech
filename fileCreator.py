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
	print("DirTwo has been created")

#create the second directory
directoryPath= Path("dirTwo")

if directoryPath.exists():
        print("DirTwo already exists. Deleting any files within...")
        subprocess.run("find dirTwo -mindepth 1 -delete", shell=True)
        
else:
        directoryPath.mkdir()
        print("DirTwo has been created")


subprocess.run("echo 'Rodgers Mwangi' > dirOne/Rodgers.txt", shell=True)
subprocess.run("echo 'Rodgers Mwangi' > dirTwo/Rodgers.txt", shell=True)
