# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов: '))
sum_num = 0
for i in range(n):
    num_div = (2 ** (- i)) * ((-1)**i)
    sum_num += num_div

print(sum_num)