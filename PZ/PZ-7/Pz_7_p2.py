#Дана строка, содержащая цифры и строчные латинские буквы. Если буквы в строке
#упорядочены по алфавиту, то вывести 0; в противном случае вывести номер первого
#символа строки, нарушающего алфавитный порядок.

strochka = input("Введите строку, содержащую цифры и строчные латинские буквы: ")

def check_alphabetical_order(input_string):
    prev_char = ''
    count = 0
    for char in input_string:
        count += 1
        if 'a' <= char <= 'z':
            if prev_char != '' and char < prev_char:
                return count
            prev_char = char
    return 0


result = check_alphabetical_order(strochka)

if result != 0:
    print('Алфавитный порядок нарушается на символе номер', result)
else:
    print('Алфавитный порядок не нарушается,', result)