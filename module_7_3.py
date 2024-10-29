import os
import time
class WordsFinder:
    file_names = []
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(punctuation, '')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words
    def find(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

print("В команде Мастера кода участников: %d !" % team1_num) # Использование %
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)) # Использование %

print("Команда Волшебники данных решила задач: {} !".format(score_2)) # Использование format()
print("Волшебники данных решили задачи за {:.1f} с !".format(team2_time)) # Использование format()

print(f"Команды решили {score_1} и {score_2} задач.") # Использование f-строк
print(f"Результат битвы: {challenge_result}") # Использование f-строк

print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.") # Использование f-строк

directory = "."
for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(root, file)
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.dirname(filepath)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')