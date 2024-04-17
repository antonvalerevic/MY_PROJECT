# шифр цезаря

language_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
language_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
step = int(input('Сдвиг шифрования'))
message = input('Enter text').upper()
new_message = ''
language = input('eng or ru')
if language == 'eng':
    for i in message:
        result = language_eng.find(i)
        new_result = result + step              #для дешифрования меняем знак на "-"
        if i in language_eng:
            new_message += language_eng[new_result]
        else:
            new_message += i
else:
    for i in message:
        result = language_eng.find(i)
        new_result = result + step              #для дешифрования меняем знак на "-"
        if i in language_ru:
            new_message += language_ru[new_result]
        else:
            new_message += i

print(new_message)