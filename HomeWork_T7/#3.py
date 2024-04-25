# Поиск палиндрома
def search_pal(str):
    return str == str[::-1]
str = ['abcba', 'defg', 'hijklm']
palindrome = list(filter(search_pal, str))

print(palindrome)