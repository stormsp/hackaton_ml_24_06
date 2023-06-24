# -*- coding: utf-8 -*-
import nltk

nltk.download('punkt')  # Загрузка ресурсов для токенизации

with open('123.txt', 'r', encoding='utf-8') as file:
    text = file.read()


output_file = "result.txt"  # Путь и имя файла для записи результата

# Токенизация текста на слова
words = nltk.word_tokenize(text)

# Запись результата в файл
with open(output_file, "w", encoding="utf-8") as file:
    file.write("\n".join(words))

print("Результат записан в файл:", output_file)

print(words)