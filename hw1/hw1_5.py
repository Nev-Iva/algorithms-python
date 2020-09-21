# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string

while True:
    num_letter = input('Введите номер буквы в английском алфавите: ')
    if (num_letter.isdigit()) and (int(num_letter) >= 1) and (int(num_letter) <= 26):
        letter_num = string.ascii_lowercase[int(num_letter) - 1]
        print('Под номером {0} находится буква {1}'.format(num_letter, letter_num))
        break
    else:
        print('Вам необходимо ввести целое число от 1 до 26.')