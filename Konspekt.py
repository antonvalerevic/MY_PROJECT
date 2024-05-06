# def calculate_index(height, weight):
#     index = weight / (height / 100)**2
#     return index
# def category_index(index):
#     if index < 18.5:
#         return "Low mass"
#     elif 18.5 <= index and index <= 24.9:
#         return "Normal mass"
#     elif 25 <= index and index <= 29.9:
#         return "Very big mass"
#     else:
#         return "Fat boy)"
#
# try:
#     height = float(input('Рост в сантиметрах:'))
#     weight = float(input('Масса в килограммах:'))
#
#     index = calculate_index(height, weight)
#     category = category_index(index)
#
#     print(f'Индекс массы тела: {index}')
#     print(f'Категория: {category}')
#
# except ValueError:
#     print('Ошибка ввода')




def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num/2
        else:
            raise ZeroDivisionError("На ноль делить нельзя, дурачок")
    else:
        raise ValueError("Неизвстная операция")

try:
    num1 = float(input("Первое число:"))
    num2 = float(input("Второе число:"))
    operation = input("Введите операцию:")

    result = calculator(num1, num2, operation)
    print(f"Результат: {result}")

except ValueError:
    print("Error")
except ZeroDivisionError as e:
    print(e)





