# Напишите программу с классом Math. При
# инициализации атрибутов нет. Реализовать методы addition,
# subtraction, multiplication и division. При передаче в методы
# двух числовых параметров нужно производить с
# параметрами соответствующие действия и печатать ответ

class Math:
    def addition(self, a, b):
        result = a + b

        print(f"The result of the addition is: {result} ")

    def subtraction(self, a, b):
        result = a - b

        print(f"The result of the substraction is: {result} ")

    def multiplication(self, a, b):
        result = a * b

        print(f"The result of the multiplication is: {result} ")

    def division(self, a, b):
        if b == 0:
            print("Error")
        else:
            result = a * b

            print(f"The result of the division is: {result} ")

math = Math()


math.addition(5, 8)
math.subtraction(5, 15)
math.multiplication(9, 17)
math.division(8, 0)
math.division(81, 9)
