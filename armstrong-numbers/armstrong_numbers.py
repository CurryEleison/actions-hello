"""
Wanted something that doesn't depend on casting the number to a string.
"""
def is_armstrong_number(number):
    digits = list(generate_digits(number))
    sz = len(digits)
    acc = sum([d**sz for d in digits])
    return acc == number

def generate_digits(number, base = 10):
    remains = number
    while remains > 0:
        yield remains % base
        remains = remains // base