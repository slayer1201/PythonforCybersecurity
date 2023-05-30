import requests
from configparser import ConfigParser
import json
import tkinter as tk
from tkinter import filedialog

# Read the INI file
config = ConfigParser()
config.read(r"C:\Users\Mahoney\OneDrive\.Programing\GitHub\PythonforCybersecurity\.IT102_Labs\TestSecrets.ini")

# Get the access token from the INI file
access_token = config.get("APIKeys", "Canvas")

base_url = "https://canvas.instructure.com/api/v1"
api_path = "/courses"
url = base_url + api_path

params = {}

headers = {
    "Authorization": f"Bearer {access_token}"
}

try:
    # Make API request to retrieve the list of courses
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        response_data = json.loads(response.content)

        # Extract the course_code for each course and print it
        for course in response_data:
            if "course_code" in course:
                course_code = course["course_code"]
                print(course_code)

        # Prompt for file path using dialog box
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        root.destroy()

        # Save the course codes to the file
        with open(file_path, "w") as file:
            for course in response_data:
                if "course_code" in course:
                    course_code = course["course_code"]
                    file.write(course_code + "\n")

        print("Course codes saved to", file_path)
    else:
        print("Failed to retrieve courses list. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("An error occurred during the request:", e)
