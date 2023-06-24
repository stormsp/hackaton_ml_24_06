import nltk
import pickle
from nltk.tokenize import sent_tokenize

# Загрузка классификатора
with open('classifier.pickle', 'rb') as file:
    classifier = pickle.load(file)

# Загрузка модуля для токенизации предложений
nltk.download('punkt')

# Считывание текста из файла
with open('example.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Сегментация текста на предложения
sentences = sent_tokenize(text)

# Представление слов в виде векторов
def extract_features(words):
    features = {word: True for word in words}
    return features

# Классификация предложений
with open('conditions.txt', 'w', encoding='utf-8') as conditions_file, \
        open('requirements.txt', 'w', encoding='utf-8') as requirements_file, \
        open('skills.txt', 'w', encoding='utf-8') as skills_file:

    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        featureset = extract_features(words)
        label = classifier.classify(featureset)

        # Запись предложения в файл
        if label == 'требования к сотруднику':
            requirements_file.write(sentence + '\n')
        elif label == 'условия работы':
            conditions_file.write(sentence + '\n')
        elif label == 'персональные навыки':
            skills_file.write(sentence + '\n')


