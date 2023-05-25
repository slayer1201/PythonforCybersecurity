import requests

response = requests.get('https://randomuser.me/api/')
data = response.json()

if 'results' in data:
    user = data['results'][0]

    name = f"{user['name']['first']} {user['name']['last']}"
    gender = user['gender']
    email = user['email']
    username = user['login']['username']
    dob = user['dob']['date']
    address = f"{user['location']['street']['number']} {user['location']['street']['name']}, {user['location']['city']}, {user['location']['state']}, {user['location']['country']}"

    print("Random User Details:")
    print(f"Name: {name}")
    print(f"Gender: {gender}")
    print(f"Email: {email}")
    print(f"Username: {username}")
    print(f"Date of Birth: {dob}")
    print(f"Address: {address}")
else:
    print("Failed to fetch user details.")
