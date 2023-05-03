
def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Whats your number: "))
if is_prime_number(number):
    print(f"{number} is prime")
else:
    print(f"{number} isn't prime")