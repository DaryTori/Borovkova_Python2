#Дана строка, содержащая цифры и строчные латинские буквы. Если буквы в строке
#упорядочены по алфавиту, то вывести 0; в противном случае вывести номер первого
#символа строки, нарушающего алфавитный порядок.

strochka = input("Введите строку, содержащую цифры и строчные латинские буквы: ")

def check_alphabetical_order(input_string):
    prev_char = ''
    count = 0
    for char in input_string:
        if 'a' <= char <= 'z':
            if prev_char != '' and char < prev_char:
                return count
            prev_char = char
        count += 1
    return 0


result = check_alphabetical_order(strochka)

print(result)