import re

def read_stop_words(file_path):
    with open(file_path, 'r') as f:
        stop_words = f.read().split()
        return [word.lower() for word in stop_words]

def censor_text(file_path, stop_words):
    with open(file_path, 'r') as f:
        text = f.read()
        for word in stop_words:
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            text = pattern.sub('*' * len(word), text)
        return text

def main():
    stop_words_file = 'C:\\Users\\Антон\\Desktop\\1 задание\\stop_words.txt'
    text_file = 'C:\\Users\\Антон\\Desktop\\1 задание\\text file.txt'

    stop_words = read_stop_words(stop_words_file)
    censored_text = censor_text(text_file, stop_words)

    print(censored_text)

if __name__ == '__main__':
    main()