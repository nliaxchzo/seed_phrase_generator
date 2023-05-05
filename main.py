import itertools
# Считываем список слов из файла
with open('wordlist.txt', 'r') as f:
    words = f.read().splitlines()

# Генерируем все возможные комбинации слов из списка
combinations = list(itertools.product(words, repeat=12))

# Сохраняем все комбинации в файл
with open('seed_phrases.txt', 'w') as f:
    for combination in combinations:
        f.write(' '.join(combination) + '\n')

print('Seed фразы успешно записаны в файл seed_phrases.txt')
