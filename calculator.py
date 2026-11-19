import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm input")
    return math.log(b, a)

def exp(a, b):

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero: 'a' must not be 0.")
    return b / a

def logarithm(a, b):
    if a <= 0:
        raise ValueError("Logarithm base 'a' must be greater than 0.")
    if a == 1:
        raise ValueError("Logarithm base 'a' cannot be 1.")
    if b <= 0:
        raise ValueError("Logarithm argument 'b' must be greater than 0.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b