# import
import requests

# define
def get_thejoke():
    url = "https://icanhazdadjoke.com/"
    payload={}
    headers = {
        'Accept': "application/json"
}
    response = requests.request("GET", url, headers=headers, data=payload)
    items = response.json() 
    return items

# Get People
thejoke = get_thejoke()

# Print
#print(thejoke)
print(thejoke["joke"])