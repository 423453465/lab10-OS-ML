# https://github.com/423453465/lab10-OS-ML
# Partner 1: Owen Staples
# Partner 2: Chengxi Li

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def multiply(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0:
        raise ValueError("Logarithm base 'a' must be greater than 0.")
    if a == 1:
        raise ValueError("Logarithm base 'a' cannot be 1.")
    if b <= 0:
        raise ValueError("Logarithm argument 'b' must be greater than 0.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
	if a < 0:
		raise ValueError("Square root 'a' cannot be negative.")
	return math.sqrt(a)

def hypotenuse(a, b):
	math.hypot(a, b)
