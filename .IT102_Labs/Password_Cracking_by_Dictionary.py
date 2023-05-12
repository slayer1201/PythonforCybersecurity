# get current directory
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import crypt

# Create Tkinter root window
root = Tk()

# Hide the root window
root.withdraw()

# Prompt the user to select a file
print("Select dictionary file")

# Display the file picker dialog
file_path = askopenfilename()

# Get the full path of the selected file
dictionary = os.path.abspath(file_path)

# Print the selected file name
print("Selected file:", dictionary)

# Ask user for hash/salt
type_salt = input("$Type$Salt$ to be matched: ")

# Ask user for hashed password
pass_hash = input("Target Password $Type$Salt$Hash: ")

# Read password list
with open(dictionary, "r") as dictionary_file:
    guesses = dictionary_file.readlines()

# Loop through each password guess
for guess in guesses:
    # Hash the guess using the hashtype / salt
    hashed_guess = crypt.crypt(guess.strip(), type_salt)
    # Compare hashed guess against the original hash
    if pass_hash == hashed_guess:
        # If match, Print and exit
        print("Password found:", guess)
        break
else:
    print("Password not found.")