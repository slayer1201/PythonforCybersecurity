# get current directory
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# Create Tkinter root window
root = Tk()

# Hide the root window
root.withdraw()

# Prompt the user to select a file
print("Select log file")

# Display the file picker dialog
file_path = askopenfilename()

# Get the full path of the selected file
log = os.path.abspath(file_path)

# Print the selected file name
print("Selected file:", log)

# Ask user for query
query = input("Look For Lines Containing: ")

# Read log file
with open(log, "r") as log_file:
    lines = log_file.readlines()

# Store found lines
found_lines = []

# Loop through each line
for line in lines:
    # Compare lines against query
    if line.find(query) != -1:
        # If match, store the line
        found_lines.append(line)

if found_lines:
    # Ask user for file name and location to save
    print("Save found lines")
    save_path = asksaveasfilename(defaultextension=".txt")

    if save_path:
        # Write found lines to the selected file
        with open(save_path, "w") as save_file:
            save_file.writelines(found_lines)
        print("Lines saved successfully.")
    else:
        print("No file selected. Lines not saved.")
else:
    print("Query not found.")
