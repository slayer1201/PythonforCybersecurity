import requests
from configparser import ConfigParser
import json

# Read the INI file
config = ConfigParser()
config.read(r"C:\Users\Mahoney\OneDrive\.Programing\GitHub\PythonforCybersecurity\.IT102_Labs\TestSecrets.ini")

# Get the access token from the INI file
access_token = config.get("APIKeys", "Canvas")

url = "https://egator.greenriver.edu/doc/api/api-docs.json"

params = {
    "enrollment_type": "student",
    "include": ["needs_grading_count", "syllabus_body", "public_description", "total_scores", "grading_periods", "term", "account", "course_progress", "sections", "storage_quota_used_mb", "total_students"],
    "state": ["available"]
}

headers = {
    "Authorization": f"Bearer {access_token}"
}

try:
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        try:
            response_data = json.loads(response.content)  # Parse the response content as JSON
            # Access the nested structure to get the list of courses
            apis = response_data.get("apis", [])
            for api in apis:
                if api.get("description") == "Courses":
                    courses_path = api.get("path")
                    break
            else:
                raise ValueError("Courses API path not found")
            
            courses_url = f"https://egator.greenriver.edu/doc/api{courses_path}"
            courses_response = requests.get(courses_url, headers=headers)
            
            if courses_response.status_code == 200:
                courses_data = json.loads(courses_response.content)
                courses = courses_data.get("courses", [])
                for course in courses:
                    course_id = course["id"]
                    course_name = course["name"]
                    # Access other course properties and perform actions
                    print("Course ID:", course_id)
                    print("Course Name:", course_name)
            else:
                print("Failed to retrieve courses. Status code:", courses_response.status_code)
        except json.JSONDecodeError as e:
            print("Failed to parse JSON response:", e)
    else:
        print("Failed to retrieve courses. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("An error occurred during the request:", e)
