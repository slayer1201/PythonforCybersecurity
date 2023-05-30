import configparser
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

def insert_api_key(key_name, key_value, save_file_path):
    config = configparser.ConfigParser()
    config.read(save_file_path)

    # Create the 'APIKeys' section if it doesn't exist
    if "APIKeys" not in config.sections():
        config.add_section("APIKeys")

    # Set the key value in the specified key name
    config.set("APIKeys", key_name, key_value)

    # Write the changes to the file
    with open(save_file_path, "w") as config_file:
        config.write(config_file)

# Prompt for the key name and key value
key_name = input("Enter the key name: ")
key_value = input("Enter the key value: ")

# Open file dialog to select the destination file path and name
Tk().withdraw()
save_file_path = asksaveasfilename(defaultextension=".ini", initialfile="secrets.ini")

if save_file_path:
    insert_api_key(key_name, key_value, save_file_path)
    print("Key inserted successfully!")
else:
    print("Operation canceled.")
