# Дан список чисел. С помощью map() получить список,
# где каждое число из исходного списка переведено в строку.
def convert_in_str(numbers):
    return list(map(str, numbers))


numbers = [1, 2, 3]

print(convert_in_str(numbers))