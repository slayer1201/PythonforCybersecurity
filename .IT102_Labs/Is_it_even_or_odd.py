#
your_number = int(input("Enter your your number: "))  # Prompt the user for a your_number and convert it to an integer

if your_number % 2 == 0:  # Check if the your_number is even (i.e., divisible by 2 with no remainder)
    print(your_number, "is even.")
else:
    print(your_number, "is NOT even.")  # If the your_number is not even, it must be odd