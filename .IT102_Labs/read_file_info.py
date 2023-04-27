# File Location
filename = "C:/Info/hackme.txt"

# Check if file exists
try:
    with open(filename, "r") as f:
        # Read and print
        print("Here is someone to hack - information:\n")
        print(f.read())
# Cant find it        
except FileNotFoundError:
    print(f"The file {filename} does not exist.")