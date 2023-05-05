import itertools
import os

# Получаем входные данные от пользователя
words = []
for i in range(8):
    word = input(f'Введите {i+1}-ое слово: ')
    words.append(word)

# Считываем слова из файла словаря
with open('dictionary.txt') as f:
    dictionary_words = f.read().splitlines()

# Генерируем все возможные уникальные комбинации слов из списка
combinations = itertools.combinations(words + dictionary_words, 12)

# Проверяем, что файл можно создать и записать
filename = 'seed_phrases.txt'
try:
    with open(filename, 'w') as f:
        pass
    os.remove(filename)
except IOError:
    print(f'Ошибка: Не удалось создать файл {filename} или нет прав на запись в этот файл')
    exit()

# Сохраняем все комбинации в файл
try:
    with open(filename, 'w') as f:
        for i, combination in enumerate(combinations):
            if i >= 52428800:
                break
            f.write(' '.join(combination) + '\n')
        print('Seed фразы успешно записаны в файл seed_phrases.txt')
except IOError:
    print('Ошибка: Не удалось записать seed фразы в файл')
