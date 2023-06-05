import requests
import hashlib
import string
import secrets
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

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

def create_sha1(plain_text):
    character_set = list(plain_text)  # Convert the plain_text string to a list of characters
    encoded_characters = []

    for character in character_set:
        while True:
            try:
                encoded_character = character.encode("utf-8")
                encoded_characters.append(encoded_character)
                break
            except UnicodeEncodeError:
                character = secrets.choice(character_set)

    encoded_text = b"".join(encoded_characters)
    result = hashlib.sha1(encoded_text)
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

    # Include similar char
    if include_similar:
        symbols += 'Il1|!'
        numbers += 'Il1'
        lowercase += 'il'
        uppercase += 'IL'

    # Include ambiguous char
    if include_ambiguous:
        symbols += '{}[]()/\\\'\"!,;:><,.'

    # Determine the set of char to be used
    character_set = []
    if include_symbols:
        character_set.extend(symbols)
    if include_numbers:
        character_set.extend(numbers)
    if include_lowercase:
        character_set.extend(lowercase)
    if include_uppercase:
        character_set.extend(uppercase)
    if include_unicode:
        character_set.extend([chr(i) for i in range(0x80, 0xFFFF)])

    # Ensure one char set selected
    if len(character_set) == 0:
        raise ValueError("No character set selected.")

    # Generate pass
    password = []

    # Add at least one symbol
    if include_symbols:
        password.append(secrets.choice(symbols))

    # Add at least one number
    if include_numbers:
        password.append(secrets.choice(numbers))

    # Add remaining characters
    for _ in range(length - 2):
        character = secrets.choice(character_set)
        password.append(character)

    # Shuffle the password
    secrets.SystemRandom().shuffle(password)

    # First character letter
    if first_char_letter:
        first_char = secrets.choice(string.ascii_letters)
        password[0] = first_char

    return ''.join(password)

def main():
    window = tk.Tk()
    window.title("Password Generator")

    include_symbols = tk.BooleanVar()
    symbols_checkbox = tk.Checkbutton(window, text="Include symbols?", variable=include_symbols)
    symbols_checkbox.grid(row=0, column=0, sticky="w")

    include_numbers = tk.BooleanVar()
    numbers_checkbox = tk.Checkbutton(window, text="Include numbers?", variable=include_numbers)
    numbers_checkbox.grid(row=1, column=0, sticky="w")

    include_lowercase = tk.BooleanVar()
    lowercase_checkbox = tk.Checkbutton(window, text="Include lowercase letters?", variable=include_lowercase)
    lowercase_checkbox.grid(row=2, column=0, sticky="w")

    include_uppercase = tk.BooleanVar()
    uppercase_checkbox = tk.Checkbutton(window, text="Include uppercase letters?", variable=include_uppercase)
    uppercase_checkbox.grid(row=3, column=0, sticky="w")

    include_unicode = tk.BooleanVar()
    unicode_checkbox = tk.Checkbutton(window, text="Include Unicode characters?", variable=include_unicode)
    unicode_checkbox.grid(row=4, column=0, sticky="w")

    include_similar = tk.BooleanVar()
    similar_checkbox = tk.Checkbutton(window, text="Include similar characters?", variable=include_similar)
    similar_checkbox.grid(row=5, column=0, sticky="w")

    include_ambiguous = tk.BooleanVar()
    ambiguous_checkbox = tk.Checkbutton(window, text="Include ambiguous characters?", variable=include_ambiguous)
    ambiguous_checkbox.grid(row=6, column=0, sticky="w")

    first_char_letter = tk.BooleanVar()
    first_char_checkbox = tk.Checkbutton(window, text="Ensure the first character is a letter?", variable=first_char_letter)
    first_char_checkbox.grid(row=7, column=0, sticky="w")

    num_passwords_label = tk.Label(window, text="Number of passwords:")
    num_passwords_label.grid(row=8, column=0, sticky="w")

    num_passwords = tk.Entry(window)
    num_passwords.grid(row=8, column=1, sticky="w")

    length_label = tk.Label(window, text="Password length (4-300):")
    length_label.grid(row=9, column=0, sticky="w")

    length = tk.Entry(window)
    length.grid(row=9, column=1, sticky="w")

    def generate_passwords():
        include_symbols_val = include_symbols.get()
        include_numbers_val = include_numbers.get()
        include_lowercase_val = include_lowercase.get()
        include_uppercase_val = include_uppercase.get()
        include_unicode_val = include_unicode.get()
        include_similar_val = include_similar.get()
        include_ambiguous_val = include_ambiguous.get()
        first_char_letter_val = first_char_letter.get()

        try:
            num_passwords_val = int(num_passwords.get())
            length_val = int(length.get())

            passwords = []
            for _ in range(num_passwords_val):
                password = generate_password(length_val, include_symbols_val, include_numbers_val,
                                             include_lowercase_val, include_uppercase_val,
                                             include_unicode_val, include_similar_val,
                                             include_ambiguous_val, first_char_letter_val)
                passwords.append(password)

            output_text.delete("1.0", "end")
            for password in passwords:
                pass_hash = create_sha1(password)
                pass_hash = pass_hash.upper()

                hash_prefix = pass_hash[:5]
                hash_postfix = pass_hash[5:]

                password_dictionary = check_pwnedpasswords(hash_prefix)

                if hash_postfix in password_dictionary:
                    output_text.insert("end", password + " Password has been compromised. It has been found this many times: ")
                    output_text.insert("end", password_dictionary[hash_postfix] + "\n")
                    output_text.insert("end", repr(password) + "\n")
                else:
                    output_text.insert("end", repr(password) + " Looks Secure!\n")

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers for number of passwords and length.")

    generate_button = tk.Button(window, text="Generate Passwords", command=generate_passwords)
    generate_button.grid(row=10, column=0, columnspan=2, pady=10)

    output_text = tk.Text(window)
    output_text.grid(row=11, column=0, columnspan=2, sticky="nsew")

    scrollbar = tk.Scrollbar(window)
    scrollbar.grid(row=11, column=2, sticky="ns")

    output_text.config(yscrollcommand=scrollbar.set)

    window.columnconfigure(0, weight=1)
    window.rowconfigure(11, weight=1)

    window.mainloop()

if __name__ == "__main__":
    main()
