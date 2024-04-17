# проверка на простое число

n = int(input("Enter number"))
if n == 2 or n == 3:
    print(f"Число {n} простое")
elif n % 2 != 0 and n % 3 != 0:
    print(f"Число {n} простое")

if n % 3 == 0 or n % 2 == 0:
    print(f"Число {n} не является простым")