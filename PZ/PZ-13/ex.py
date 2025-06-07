#В двумерном списке найти сумму и произведение элементов строки N (N задать с
#клавиатуры).

import random
from functools import reduce

n = input('Размер матрицы: ')
n = int(n)

matrix = [[random.randint(1, 50) for ele in range(n)] for strok in range(n)]
print("Матрица:")
for strok in matrix:
    print(strok)

k = int(input('Номер строки: '))

n_str = matrix[k-1]
summa = reduce(lambda x, y: x + y, n_str) 
proizv = reduce(lambda x, y: x * y, n_str)

print('Сумма строки:', summa)
print('Произведение строки:', proizv)