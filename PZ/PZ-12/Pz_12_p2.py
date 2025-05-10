#Составить генератор (yield), который выводит из строки только цифры.
stroka = input("Введите строку: ")
def cifri(s): 
    yield from [n for n in s if n.isdigit()]
print(*list(cifri(stroka)))