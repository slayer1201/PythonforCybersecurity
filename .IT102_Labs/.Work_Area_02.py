import requests
import hashlib

def check_pwnedpasswords(hash_prefix):
    url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
    response = requests.get(url)
    response.raise_for_status()
    pwnd_dict = {item.split(":")[0]: item.split(":")[1] for item in response.text.splitlines()}
    return pwnd_dict

def create_sha1(plain_text):
    digest = hashlib.sha1(plain_text.encode()).hexdigest().upper()
    return digest

password = input("What password do you want to test") or "qwerty"

pass_hash = create_sha1(password)

hash_prefix = pass_hash[:5]
hash_postfix = pass_hash[5:]

try:
    password_dictionary = check_pwnedpasswords(hash_prefix)
    if hash_postfix in password_dictionary:
        print("Password has been compromised. It has been found this many times:")
        print(password_dictionary[hash_postfix])
    else:
        print("Password looks secure!")
except requests.exceptions.HTTPError as e:
    print("An error occurred while checking the password:", str(e))
