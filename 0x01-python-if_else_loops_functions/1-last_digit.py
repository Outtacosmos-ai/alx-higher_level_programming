import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and greater than 5.")
elif 0 < last_digit < 6:
    print(f"Last digit of {number} is {last_digit} and less than 6 and not 0.")
else:
    print(f"Last digit of {number} is 0 and is 0.")
