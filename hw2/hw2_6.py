# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или
# меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.

import random

secret_num = random.randint(0, 100)
i = 1
attempt_num = 10
answer_true = 0
while i <= attempt_num:
    user_num = int(input('Попытка № {0}. Введите число: '.format(i)))
    i += 1
    if user_num < secret_num:
        print('Ваше число меньше загаданного.')
    elif user_num > secret_num:
        print('Ваше число больше загаданного.')
    else:
        answer_true = 1
        print('Вы угадали.')
        break

if answer_true == 0:
    print('Вы не смогли угадать число за {0} попыток. Загаданное число было: {1}.'.format(attempt_num, secret_num))
else:
    print('Победа.')