# Последовательность Фибоначи

def fibonacci(n):
    fib = []

    a, b = 0, 1

    for _ in range(n):
        fib.append(a)
        a, b = b, a + b

    return fib


n = int(input("Введите количество чисел последовательности Фибоначчи: "))
fib = fibonacci(n)
print(f"Последовательность Фибоначчи из {n} чисел: {fib}")
