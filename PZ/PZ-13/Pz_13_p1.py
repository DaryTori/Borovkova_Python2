# В квадратной матрице все элементы на главной диагонали увеличить в 2 раза.

import random

def udvoi_matrix(mx):
    for i in range(len(mx)):
        for j in range(len(mx)):
            if i == j:
                mx[i][j] *= 2
    return mx

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

matrix = udvoi_matrix(matrix)
print('Изменённая матрица:')
for strok in matrix:
    print(strok)