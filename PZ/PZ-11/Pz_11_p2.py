#Из предложенного текстового файла (text18-4.txt) вывести на экран его содержимое,
#количество символов, принадлежащих к группе букв. Сформировать новый файл, в
#который поместить текст в стихотворной форме предварительно заменив символы верхнего
#регистра на нижний.

count = 0
for i in open('text18-4.txt', 'r', encoding="utf-8"):
    print(i, end='')
    for j in i:
        if 'а' <= j <= 'я' or 'А' <= j <= 'Я':
            count += 1
print(end='\n')
print('Количество символов, принадлежащих к группе букв:', count)

f1 = open('text18-4.txt', encoding='utf-8')
lines = f1.readlines()
f1.close()

f2 = open('text18-4.txt', 'w')
lines = ''.join(lines)
f2.writelines(lines.lower())
f2.close()