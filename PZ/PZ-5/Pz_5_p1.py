#Составить функцию, которая выполнит суммирования числового ряда.

def su(lst):
    summa = 0
    for i in lst:
        summa += i
    return summa

els = []

el = input("Введите число или 'стоп' чтобы прекратить ввод: ")
while el != "стоп": # обработка исключений + добавление элементов в список
    try:
        el = float(el)
        els.append(el)
        el = input("Введите число или 'стоп' чтобы прекратить ввод: ")
    except ValueError:
        el = input("Введите число или 'стоп' чтобы прекратить ввод: ")

print("Сумма чисел равна", su(els))