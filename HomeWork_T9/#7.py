def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

with open("C:\\Users\\Антон\\Desktop\\1 задание\\Hello.txt", "r") as file:
    lines = file.readlines()

encrypted_lines = []
for i, line in enumerate(lines):
    shift = i + 1
    encrypted_line = caesar_encrypt(line.strip(), shift)
    encrypted_lines.append(encrypted_line)

print("\n".join(encrypted_lines))

