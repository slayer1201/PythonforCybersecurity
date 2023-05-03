# Prompt user for message
initial_message = input("What is your message? ")
final_message = ""
# Hello World --> HELLO WORLD
initial_message = initial_message.upper()

# loop through each letter of message
for character in initial_message:
    # Convert letter to number
    ascii_number = ord(character)
    # if number is a valid letter
    if ascii_number >= 65 and ascii_number <= 90:
    # add 13 to number 
        ascii_number = ascii_number + 13 
        # if beyond "Z" then....
        if ascii_number > 90:
            # subtract 26
            ascii_number = ascii_number - 26
    # Convert Number to letter
    final_message = final_message + chr(ascii_number)

# Print Message
    print(final_message)