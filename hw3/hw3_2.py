# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

import random

random_list = [random.randint(0, 20) for el in range(1, 7)]
print(random_list)
final_list = []

for i in range(len(random_list)):
    if random_list[i] % 2 == 0:
        final_list.append(i)
print(final_list)