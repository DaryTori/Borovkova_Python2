#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Минимальный элемент:
#Квадраты четных элементов:
#Сумма квадратов четных элементов:
#Среднее арифметическое суммы квадратов четных элементов:

numbers = ['-100 99 3 44 -56 -7 -4543 878 34']
file_num = open('numbers.txt', 'w')
file_num.writelines(numbers)
file_num.close()

file_num_2 = open('numbers2.txt', 'w')
file_num_2.write('Исходные данные: ')
file_num_2.write('\n')
file_num_2.writelines(numbers)
file_num_2.close()

file_num = open('numbers.txt')
spisok_num = file_num.read()
spisok_num = spisok_num.split()
for i in range(len(spisok_num)):
    spisok_num[i] = int(spisok_num[i])
file_num.close()

file_num = open('numbers.txt')
min = spisok_num[0]
even = []
for i in range(len(spisok_num)):
    min = min if min < spisok_num[i] else spisok_num[i]
    if spisok_num[i] % 2 == 0:
        even.append(spisok_num[i] ** 2)

sum_even = 0
for i in even:
    sum_even += i

average = sum_even / len(even)

file_num_2 = open('numbers2.txt', 'a') # открываем файл для дозаписи
file_num_2.write('\n')
print(' Количество элементов: ', len(spisok_num), '\n', 'Минимальный элемент: ', min, '\n'
      ' Квадраты четных элементов: ', *even, '\n', 'Сумма квадратов четных элементов:', sum_even, '\n',
      'Среднее арифметическое суммы квадратов четных элементов:', average, file=file_num_2)
file_num_2.close()