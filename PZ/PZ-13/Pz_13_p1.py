# В квадратной матрице все элементы на главной диагонали увеличить в 2 раза.

import random

n = input("Введите размер матрицы: ")
while type(n) != int:  # обработка исключений
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите размер матрицы: ")

matrix = [[random.randint(1, 50) for ele in range(n)] for strok in range(n)]

print("Изначальная матрица:")
for strok in matrix:
    print(strok)

matrix = [[ele * 2 if i == j else ele for i, ele in enumerate(strok)] for j, strok in enumerate(matrix)]
print('Изменённая матрица:')
for strok in matrix:
    print(strok)