print('abc' + 'dec')
a = 'stroka1'
b = 'stroka2'
e = ' '
print(a+e+b)
print(len(a))
if 'a' in b:
    print('yes')

d = 'stroka1 stroka2'
e = 'STROKA1 STROKA2'
f = '1234546'
print(d[6])
print(d[5:9])
print(d[1:-1:2])

print(d.upper())
print(e.lower())
print(d.count('k'))
print(d.count('k', 1, 8))
print(d.find('o'))
print(d.rfind('o'))
print(d.index('k'))
print((d.replace('k', 'f')))

if f.isdigit():
    print('YESS')

if e.isalpha():
    print('Yess')
else:
    print('No')

print(e.split())