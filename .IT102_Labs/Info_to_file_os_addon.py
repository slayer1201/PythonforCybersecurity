#Import os
import os

# Ask for info
name = input("What is your name? ")
color = input("What is your favorite color? ")
pet_name = input("What was your first pet's name? ")
mother_maiden_name = input("What is your mother's maiden name? ")
elementary_school = input("What elementary school did you attend? ")

# Laugh at them
print("Thanks Sucker!")

# Create directory if it doesn't exist
directory = "C:/Info"
if not os.path.exists(directory):
    os.makedirs(directory)

# Append info
filename = "C:/Info/hackme.txt"
with open(filename, "a") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Favorite color: {color}\n")
    f.write(f"First pet's name: {pet_name}\n")
    f.write(f"Mother's maiden name: {mother_maiden_name}\n")
    f.write(f"Elementary school: {elementary_school}\n")
    
print("Info added to hackme.txt")