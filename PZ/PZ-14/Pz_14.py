#Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
#корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
#86532547891), а во второй с некорректными номерами телефонов. Посчитать
#Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
#корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
#86532547891), а во второй с некорректными номерами телефонов. Посчитать
#полученные строки в каждом файле.

import re

with open("hotline.txt", "r", encoding="utf-8") as file:
    stroki = file.readlines()

phone = re.compile(r'\d{11}')

correct_phones = []
incorrect_phones = []

for stroka in stroki:
    if phone.search(stroka):
        correct_phones.append(stroka)
    else:
        incorrect_phones.append(stroka)

with open("correct.txt", "w", encoding="utf-8") as f:
    f.writelines(correct_phones)

with open("incorrect.txt", "w", encoding="utf-8") as f:
    f.writelines(incorrect_phones)

print("Корректных номеров:", len(correct_phones))
print("Некорректных номеров:", len(incorrect_phones))