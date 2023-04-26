#Loop Function
def send_message(message):
    for i in range(10):
        print(message)

# yes or no
good_day = input("Is today a good day? (y/n) ")

# Check day & call send_message function
if good_day == "y" or good_day == "yes":
    send_message("Yes it is")
else:
    send_message("I guess it's not")