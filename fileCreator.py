#!/bin/python3
import subprocess
from pathlib import Path

# FORGET THE CODE, WE ARE ONLY PRINTING OUR NAMES BELOW HERE TO DEMO GIT.
#print("Amara Nyanzi")


#print("Eve Candy")


#<<<<<<< HEAD
#print("Mathew Kasanga") #<-- Add name here
#print("Name: Mathew") #<-- Add name here
#print("Name: Kasanga")#<-- Add name here
#======
#print("Mathew Kasanga")

#>>>>>>> bcac37202b1d4ff966fafe0654a7c71e9d69bfe4

#print("Steve Muturi") 


#print("Dennis Musyimi")


# -------------------------
# Create the first directory
# -------------------------

directoryPath = Path("dirOne")

if directoryPath.exists():
     print("DirOne already exists. Deleting any files within...")
     subprocess.run("find dirOne -mindepth 1 -delete", shell=True)
else:
     directoryPath.mkdir()
     print("DirOne has been created")

# -------------------------
# Create the second directory
# -------------------------

directoryPath = Path("dirTwo")

if directoryPath.exists():
     print("DirTwo already exists. Deleting any files within...")
     subprocess.run("find dirTwo -mindepth 1 -delete", shell=True)
else:
     directoryPath.mkdir()
     print("DirTwo has been created")

# -------------------------
# Create text files
# -------------------------

# TO DO: PLEASE PUT YOUR NAMES IN THIS ARRAY
fullNames = [
    "Eve Candy",
    "Amara Nyanzi",
    "Rodgers Mwangi",
    "Steve Muturi",
    "Dennis Musyimi",  
    "Hopemidah kendi",
    "Mathew kasanga",
    "Sharon Opudo"

]

for name in fullNames:
  first_name = first_name = name.split()[0]
  file_name = f"{first_name}.txt"
  subprocess.run(f"echo '{name}' > dirOne/{file_name}", shell=True)
  subprocess.run(f"echo '{name}' > dirTwo/{file_name}", shell=True)

print("txt files created")
