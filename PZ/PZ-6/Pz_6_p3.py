# Дан список размера N (N — четное число).
# Поменять местами его первый элемент со вторым, третий — с четвертым и т. д.

import random


n = input("Введите длину списка (число должно быть чётным): ")
while type(n) != int:  # обработка исключений
    try:
        n = int(n)
        while n % 2 != 0:  # приведение к чётному числу
            print("Длинна списка должна быть чётной!")
            n = input("Введите длину списка (число должно быть чётным): ")
            while type(n) != int:  # обработка исключений
                try:
                    n = int(n)
                except ValueError:
                    print("Неправильно ввели!")
                    n = input("Введите длину списка (число должно быть чётным): ")
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите длину списка (число должно быть чётным): ")


spisoc = []
i = 0
while i < n:
    spisoc.append(random.randint(0, 100))
    i += 1

print("Исходный список:", spisoc)
for j in range(0, len(spisoc), 2):
    spisoc[j], spisoc[j + 1] = spisoc[j + 1], spisoc[j]
print("Список после обмена:", spisoc)