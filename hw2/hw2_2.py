# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

n = (input('Введите число: '))
even_num = 0
uneven_num = 0
for i in range(len(n)):
    num_int = int(n[i])
    if num_int % 2 != 0:
        uneven_num += 1
    else:
        even_num += 1
print('В числе {0}: {1} четных цифр и {2} нечетных цифр'.format(n, even_num, uneven_num))
