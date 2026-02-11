#!/bin/python3
import subprocess
from pathlib import Path

# FORGET THE CODE, WE ARE ONLY PRINTING OUR NAMES BELOW HERE TO DEMO GIT.
<<<<<<< HEAD
#print("Amara Nyanzi")


#print("Eve Candy")


#print("Mathew Kasanga")


#print("Steve Muturi")   #<-- Add name here

#print("Dennis Musyimi")
=======
# print("Amara Nyanzi")


# print("Eve Candy")


# print("Mathew Kasanga")


# print("Steve Muturi")   #<-- Add name here

# print("Dennis Musyimi")
>>>>>>> a7f7c44 (Array and Loop Implementation)


# -------------------------
# Create the first directory
# -------------------------

directoryPath = Path("dirOne")

if directoryPath.exists():
<<<<<<< HEAD
     print("DirOne already exists. Deleting any files within...")
     subprocess.run("find dirOne -mindepth 1 -delete", shell=True)
else:
     directoryPath.mkdir()
     print("DirOne has been created")
=======
    print("DirOne already exists. Deleting any files within...")
    subprocess.run("find dirOne -mindepth 1 -delete", shell=True)
else:
    directoryPath.mkdir()
    print("DirOne has been created")
>>>>>>> a7f7c44 (Array and Loop Implementation)

# -------------------------
# Create the second directory
# -------------------------

directoryPath = Path("dirTwo")

if directoryPath.exists():
<<<<<<< HEAD
     print("DirTwo already exists. Deleting any files within...")
     subprocess.run("find dirTwo -mindepth 1 -delete", shell=True)
else:
     directoryPath.mkdir()
     print("DirTwo has been created")
=======
    print("DirTwo already exists. Deleting any files within...")
    subprocess.run("find dirTwo -mindepth 1 -delete", shell=True)
else:
    directoryPath.mkdir()
    print("DirTwo has been created")
>>>>>>> a7f7c44 (Array and Loop Implementation)

# -------------------------
# Create text files
# -------------------------

<<<<<<< HEAD
name = "Sharon Opudo"
filename = "Sharon.txt"

subprocess.run(f"echo '{name}' > dirOne/{filename}", shell=True)
subprocess.run(f"echo '{name}' > dirTwo/{filename}", shell=True)

subprocess.run("echo 'Rodgers Mwangi' > dirOne/Rodgers.txt", shell=True)
subprocess.run("echo 'Rodgers Mwangi' > dirTwo/Rodgers.txt", shell=True)

=======
# TO DO: PLEASE PUT YOUR NAMES IN THIS ARRAY
fullNames = [
    "Amara Nyanzi",
    "Someone else", #Replace


]

for name in fullNames:
  first_name = first_name = name.split()[0]
  file_name = f"{first_name}.txt"
  subprocess.run(f"echo '{name}' > dirOne/{file_name}", shell=True)
  subprocess.run(f"echo '{name}' > dirTwo/{file_name}", shell=True)
>>>>>>> a7f7c44 (Array and Loop Implementation)

print("txt files created")
