# Is Divisable By

# Creat Function
def is_divisible(number, divisor):
    return number % divisor == 0

# Variables
number = int(input("Enter a Number: "))
divisor = int(input("Enter a Divisor: "))

if is_divisible(number, divisor):
    # True
    print(number, "Is Divisible By", divisor)
else:
    # False
    print(number, "Is Not Divisible By", divisor)