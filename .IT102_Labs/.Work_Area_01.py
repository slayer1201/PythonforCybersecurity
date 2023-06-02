import requests
import hashlib
import random
import string

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

def generate_password(length, include_symbols=True, include_numbers=True,
                      include_lowercase=True, include_uppercase=True,
                      include_unicode=True, include_similar=True,
                      include_ambiguous=True, first_char_letter=True):
    # Define char sets
    symbols = "!@#$%^&*()_-+=~`[]{}\\|:;\"'<>,.?/"
    numbers = "0123456789"
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    # Include sim char
    if include_similar:
        symbols += 'Il1|!'
        numbers += 'Il1'
        lowercase += 'il'
        uppercase += 'IL'

    # Include ambiguous char
    if include_ambiguous:
        symbols += '{}[]()/\\\'\"!,;:><,.'

    # Determine the set of char to be used
    character_set = ''
    if include_symbols:
        character_set += symbols
    if include_numbers:
        character_set += numbers
    if include_lowercase:
        character_set += lowercase
    if include_uppercase:
        character_set += uppercase
    if include_unicode:
        character_set += ''.join(chr(i) for i in range(0x80, 0xFFFF))

    # Ensure one char set selected
    if len(character_set) == 0:
        raise ValueError("No character set selected.")

    # Generate pass
    password = ''.join(random.choice(character_set) for _ in range(length - 1))
    
    # first character letter
    if first_char_letter:
        password = random.choice(string.ascii_letters) + password

    return password

def prompt_yes_no(message):
    while True:
        response = input(f"{message} [y/n]: ")
        if response.lower() == 'y':
            return True
        elif response.lower() == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def prompt_length():
    while True:
        length = input("Enter password length (4-300): ")
        if length.isdigit() and 4 <= int(length) <= 300:
            return int(length) + 1  # Add 1 to the entered length
        else:
            print("Invalid length. Please enter a number between 4 and 300.")

def main():
    length = prompt_length()
    include_symbols = prompt_yes_no("Include symbols?")
    include_numbers = prompt_yes_no("Include numbers?")
    include_lowercase = prompt_yes_no("Include lowercase letters?")
    include_uppercase = prompt_yes_no("Include uppercase letters?")
    include_unicode = prompt_yes_no("Include Unicode char?")
    include_similar = prompt_yes_no("Include similar char?")
    include_ambiguous = prompt_yes_no("Include ambiguous char?")
    first_char_letter = prompt_yes_no("Ensure the first character is a letter?")

    num_passwords = 1
    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length, include_symbols, include_numbers,
                                     include_lowercase, include_uppercase,
                                     include_unicode, include_similar,
                                     include_ambiguous, first_char_letter)
        passwords.append(password)


    # Print
    print("Generated Passwords:")
    for password in passwords:

        pass_hash = create_sha1(password)
        pass_hash = pass_hash.upper()

        hash_prefix = pass_hash[:5]
        hash_postfix = pass_hash[5:]

        password_dictionary = check_pwnedpasswords(hash_prefix)

        if hash_postfix in password_dictionary:
            print(password + " Password has been compromised. It has been found this many times: ")
            print (password_dictionary [hash_postfix])
            print(repr(password))
        else:
            print(password + " Look Secure!")

if __name__ == "__main__":
    main()
