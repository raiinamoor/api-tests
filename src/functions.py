from math import sqrt, floor


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b

    
def divide(a: float, b: float) -> float:
    return a / b


def is_prime(number: int) -> bool:
    for i in range(2, floor(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
