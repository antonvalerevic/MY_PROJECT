with open(r'C:\Users\Антон\Desktop\1 задание\Notes.txt', 'r') as file:
    for line in file:
        name, score = line.strip().split(' - ')
        score = int(score.split(': ')[1])
        if score < 3:
            print(name)

