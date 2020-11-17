# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

random_list = [random.randint(-20, 20) for el in range(1, 15)]
print(random_list)
max_elem = 0
min_elem = 0
i_max = 0
i_min = 0
for i in range(len(random_list)):
    if random_list[i] > random_list[i_max]:
        max_elem = random_list[i]
        i_max = i
    elif random_list[i] < random_list[i_min]:
        min_elem = random_list[i]
        i_min = i

print('Максимальный элемент списка {0} на позиции {1} (нумерация с 0)'.format(max_elem, i_max))
print('Минимальный элемент списка {0} на позиции {1} (нумерация с 0)'.format(min_elem, i_min))

max_value = random_list[i_max]
random_list[i_max] = random_list[i_min]
random_list[i_min] = max_value

print(random_list)