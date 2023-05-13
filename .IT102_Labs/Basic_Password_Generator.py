import random
import string
characters = string.ascii_letters + string.digits + string.punctuation
temp = random.sample(characters, 15)
password = "".join(temp)

print(password)