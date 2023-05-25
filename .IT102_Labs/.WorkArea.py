# 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

import requests
import configparser

def get_api_key(key_name):
    config = configparser.ConfigParser()

    config.read("/home/justincase/secrets.ini")

    api_key = config["APIKeys"][key_name]
    return api_key

token = get_api_key('GitHub')

url = "https://api.github.com/user/repos"

payload={}
headers = {
        'Authorization': token
}

response = requests.request("GET", url, headers=headers, data=payload)

print (response.text)