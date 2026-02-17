#!/bin/python3

# Simple test script

names = [
    "Eve Candy",
    "Amara Nyanzi",
    "Rodgers Mwangi",
    "Steve Muturi",
    "Dennis Musyimi",
    "Hopemidah Kendi",
    "Mathew Kasanga",
    "Sharon Opudo"
]

print("Running name test...\n")

for name in names:
    first_name = name.split()[0]
    print(f"Full Name: {name}")
    print(f"First Name: {first_name}")
    print("------")

print("\nTest complete.")
