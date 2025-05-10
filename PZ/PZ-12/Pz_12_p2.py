#Составить генератор (yield), который выводит из строки только цифры.
stroka = input("Введите строку: ")
def cifri(st): 
    yield from [n for n in st if n.isdigit()]
print(*list(cifri(stroka)))