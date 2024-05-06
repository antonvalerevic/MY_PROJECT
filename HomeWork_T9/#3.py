import collections


with open("C:\\Users\\Антон\\Desktop\\1 задание\\Новый текстовый документ.txt", "r") as input_file:

    lines = input_file.readlines()


with open("#3_output.txt", "w") as output_file:

    for line in lines:

        line = line.strip()

        words = line.split()

        word_freq = collections.Counter(words)

        most_frequent_word = max(word_freq, key=word_freq.get)

        output_file.write(f"Most frequent word in this line: {most_frequent_word} ({word_freq[most_frequent_word]})\n")