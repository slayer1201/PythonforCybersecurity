# import
import requests
import json

# efine
def get_people_in_space():
    url = "http://api.open-notify.org/astros.json"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    items = response.json() 
    return items

# Get People
astronauts = get_people_in_space()

# Print
print(astronauts)
print(json.dumps(astronauts, indent=2))
print( 'There are {0} people in space right now'.format(astronauts))
print(astronauts["people"][0])
print("The first person is {0} on the craft {1}".format(astronauts["people"][0]["name"], astronauts["people"][0]["craft"]))

print("full list of people in space")
for person in astronauts["people"]:
    print(person["name"])