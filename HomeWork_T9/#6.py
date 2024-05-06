import re

with open('C:\\Users\\Антон\\Desktop\\1 задание\\6 zadanie.txt', 'r') as file:
    content = file.read()

numbers = re.findall(r'\d+', content)
sum_of_numbers = sum(int(num) for num in numbers)

print(sum_of_numbers)