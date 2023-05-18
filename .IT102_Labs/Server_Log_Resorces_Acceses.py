from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from collections import Counter

# Create Tkinter window
root = Tk()

# Hide window
root.withdraw()

# Prompt user to select file
print("Select log file")

# Display dialog
file_path = askopenfilename()

# Get full path of selected file
log = os.path.abspath(file_path)

# Print selected filename
print("Selected file:", log)

# Read log file
with open(log, "r") as log_file:
    lines = log_file.readlines()

# Extract resources accessed from log
resources = []
for line in lines:
    # resource is enclosed in double quotes after the GET method
    start_index = line.find('GET') + 4
    end_index = line.find('"', start_index)
    resource = line[start_index:end_index]
    resources.append(resource)

# Count the occurrences
resource_counts = Counter(resources)

# Prompt the user to enter a name and location to save the report
print("Save report")
save_path = asksaveasfilename(defaultextension=".txt")

if save_path:
    # Sort descending order
    sorted_resources = sorted(resource_counts.items(), key=lambda x: x[1], reverse=True)

    # Write report to selected file
    with open(save_path, "w") as save_file:
        for resource, count in sorted_resources:
            save_file.write(f"Count: {count}, Resource: {resource}\n")
    print("Report saved successfully.")
else:
    print("No file selected. Report not saved.")
