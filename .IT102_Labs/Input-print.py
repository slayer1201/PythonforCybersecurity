# A simple "Hello World" script in python
# Created by John Mahoney, 4/11/2023
your_name = input("What is your name? ")
print("Hello {0}".format(your_name))
print("Today is going to be a great day!")

# Age Question +2
your_age = int(input("What is your age? "))
your_age = your_age+2
print("In 2 years, you will be:", your_age, "years old.")

message = "I am the very model of the modern major general"
message_length = len(message)
updated_message = ""
for i in range(message_length):
    letter = message[i]
    if i % 2 == 0:
        letter = letter.swapcase()
    updated_message += letter
print(updated_message)
# Prints: i Am tHe vErY MoDeL Of tHe mOdErN MaJoR GeNeRaL

name = input("enter your name: ")

def greet(person):
         print("Hi,", person)
greet(name)
# Prints ur name