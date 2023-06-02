import requests
import hashlib
import random
import string

def check_pwnedpasswords(hash_prefix):
    url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
    response = requests.get(url)
    response.raise_for_status()
    pwnd_dict = {item.split(":")[0]: item.split(":")[1] for item in response.text.splitlines()}
    return pwnd_dict

def create_sha1(plain_text):
    digest = hashlib.sha1(plain_text.encode()).hexdigest().upper()
    return digest

def generate_password(length, include_symbols=True, include_numbers=True,
                      include_lowercase=True, include_uppercase=True,
                      include_unicode=True, include_similar=True,
                      include_ambiguous=True, first_char_letter=True):
    symbols = "!@#$%^&*()_-+=~`[]{}\\|:;\"'<>,.?/"
    numbers = "0123456789"
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    if include_similar:
        symbols += 'Il1|!'
        numbers += 'Il1'
        lowercase += 'il'
        uppercase += 'IL'

    if include_ambiguous:
        symbols += '{}[]()/\\\'\"!,;:><,.'

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

    if len(character_set) == 0:
        raise ValueError("No character set selected.")

    password = ''.join(random.choice(character_set) for _ in range(length - 1))

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
            return int(length)
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

    for _ in range(num_passwords):
        password = generate_password(length, include_symbols, include_numbers,
                                     include_lowercase, include_uppercase,
                                     include_unicode, include_similar,
                                     include_ambiguous, first_char_letter)

        pass_hash = create_sha1(password)
        hash_prefix = pass_hash[:5]
        hash_postfix = pass_hash[5:]

        try:
            password_dictionary = check_pwnedpasswords(hash_prefix)
            if hash_postfix in password_dictionary:
                print("Password has been compromised. It has been found this many times:")
                print("Password:", password)
                print("Occurrences:", password_dictionary[hash_postfix])
            else:
                print("Password looks secure!")
        except requests.exceptions.HTTPError as e:
            print("An error occurred while checking the password:", str(e))



if __name__ == "__main__":
    main()

