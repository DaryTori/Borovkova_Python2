#Дано целое число A. Проверить истинность высказывания: «Число A является
#четным»

a = input('Введите целое число A: ')

while type(a) != int: # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input('Введите целое число: ')

if a % 2 == 0:
    print("Число A является четным")
else:
    print("Число A не явлsяется четным")