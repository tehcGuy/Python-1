# Create a function that takes a number as input and returns the string‚The number of cookies is: #
# if and only if the number is smaller or equal to 9 or ‚too many cookies’ if the number is greater than 9
import sys


def greet(amount_cookies_string):
    amount_cookies = int(amount_cookies_string)

    if amount_cookies <= 9:
        print("The number of cookies is:", amount_cookies)
    else:
        print('too many cookies')


amount_cookies_string = sys.argv[1]
greet(amount_cookies_string)
