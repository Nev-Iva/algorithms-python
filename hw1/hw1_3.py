# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random
import string


def is_num(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


while True:
    bot_bord_int = (input('Введите нижнюю границу (целое число): '))
    up_bord_int = (input('Введите верхнюю границу (целое число): '))
    if (bot_bord_int.isdigit()) and (up_bord_int.isdigit()):
        bot_bord_int = int(bot_bord_int)
        up_bord_int = int(up_bord_int)
        print(random.randint(bot_bord_int, up_bord_int))
        break
    else:
        print('Необходимо ввести именно числа.')

while True:
    bot_bord_float = (input('Введите нижнюю границу (вещественное число): '))
    up_bord_float = (input('Введите верхнюю границу (вещественное число): '))
    if is_num(bot_bord_float) and is_num(up_bord_float):
        bot_bord_float = float(bot_bord_float)
        up_bord_float = float(up_bord_float)
        print(random.uniform(bot_bord_float, up_bord_float))
        break
    else:
        print('Необходимо ввести именно числа.')

while True:
    bot_symbol = input('Введите первый символ: ')
    up_symbol = input('Введите второй символ: ')
    if (bot_symbol.lower() in string.ascii_lowercase) and (up_symbol.lower() in string.ascii_lowercase) and (string.ascii_lowercase.find(bot_symbol.lower()) < string.ascii_lowercase.find(up_symbol.lower())):
        bot_symbol = bot_symbol.lower()
        up_symbol = up_symbol.lower()
        index_first = string.ascii_lowercase.find(bot_symbol)
        index_second = string.ascii_lowercase.find(up_symbol)
        str_find = string.ascii_lowercase[index_first: index_second + 1]
        str_list = []
        for el in str_find:
            str_list.append(el)
        print(random.choice(str_list))
        break
    else:
        print('Ошибка. Введите английские символы по порядку.')