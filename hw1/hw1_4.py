# 4. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

import string

while True:
    first_letter = input('Введите первую буквы: ')
    second_letter = input('Введите вторую букву: ')
    if first_letter in string.ascii_letters and second_letter in string.ascii_letters:
        first_letter_low = first_letter.lower()
        second_letter_low = second_letter.lower()
        fl_pos = string.ascii_lowercase.find(first_letter_low) + 1
        sl_pos = string.ascii_lowercase.find(second_letter_low) + 1
        print('Буква - позиция: {0} - {1}, {2} - {3}'.format(first_letter, fl_pos, second_letter_low, sl_pos))
        break
    else:
        print('Вы должны ввести английские буквы.')