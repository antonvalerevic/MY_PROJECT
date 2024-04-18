# перевод из десятичной системы в двоичную


# n = int(input('Enter number'))
# print(f"The binary equivalent of {n} is", bin(n))


def convert_dec_in_bin(n):
    bin_num = bin(n)
    return bin_num

dec_num = 10
bin_num = convert_dec_in_bin(dec_num)
bin_n = bin_num.replace('0b', '')

print(f'The binary equivalent of {dec_num} is, {bin_n}')


