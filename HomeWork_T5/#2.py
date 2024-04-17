# Разложение cos(x)
import math

def cosine(x, n=10):
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    return result

x = 1  # угол в радианах
n = 10  # количество членов в ряде Тейлора
cos_x = cosine(x, n)
print(f"cos({x}) ≈ {cos_x}")
print(f"cos({x}) ≈ {math.cos(x)}")