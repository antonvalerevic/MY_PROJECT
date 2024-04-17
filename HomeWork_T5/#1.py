# Разложение sin(x)
import math


def sin(x):
    result = 0
    for n in range(10):
        result += ((-1) ** n) * x ** (2 * n + 1) / math.factorial(2 * n + 1)

    return result


x = 1
print("sin({}) ≈ {}".format(x, sin(x)))