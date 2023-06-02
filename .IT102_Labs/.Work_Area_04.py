import requests
import hashlib

def check_pwnedpasswords(hash_prefix):
    url = "https://api.pwnedpasswords.com/range/" + hash_prefix
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    pwnd_list = response.text.splitlines()
    pwnd_dict = {}
    for item in pwnd_list:
        split_items = item.split(":")
        pwnd_dict[split_items[0]] = split_items[1]
    return pwnd_dict
    
def create_sha1 (plain_text):
    encode_text = plain_text.encode()
    result = hashlib.sha1(encode_text)
    digest = result.hexdigest()
    return digest

password = input("What password do you want to test: ") or "qwerty"

pass_hash = create_sha1(password)
pass_hash = pass_hash.upper()

hash_prefix = pass_hash[:5]
hash_postfix = pass_hash[5:]

password_dictionary = check_pwnedpasswords(hash_prefix)

if hash_postfix in password_dictionary:
    print(password + " has been compromised. It has been found this many times: ")
    print(password_dictionary[hash_postfix])
else:
    print(password + " Look Secure!")


