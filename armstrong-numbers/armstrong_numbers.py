"""
Wanted something that doesn't depend on casting the number to a string.
"""
def is_armstrong_number(number):
    """Test if a number is an armstrong number"""
    digits = list(generate_digits(number))
    input_size = len(digits)
    acc = sum([d**input_size for d in digits])
    return acc == number

def generate_digits(number, base = 10):
    """Generate digits in a given base"""
    remains = number
    while remains > 0:
        yield remains % base
        remains = remains // base
