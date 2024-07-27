import re

# Функция для проверки, содержит ли строка только цифры и запятые
def is_numeric_line(line):
    return bool(re.match(r'^[\d,.\- Е ]+$', line.strip()))

# Чтение файла и фильтрация строк
with open('work.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Запись только тех строк, которые не содержат только цифры и запятые
with open('cleardata.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        if not is_numeric_line(line):
            file.write(line)
