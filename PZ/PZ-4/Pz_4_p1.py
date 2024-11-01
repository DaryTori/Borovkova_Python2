#Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг конфет.

price = input("Введите цену конфет: ")

while type(price) != float: # обработка исключений
    try:
        price = float(price)
    except ValueError:
        print("Неправильно ввели!")
        price = input("Введите цену конфет: ")

w = 1
while w <= 10:
    print('Вес', w, 'кг конфет равен:', price * w)
    w += 1
