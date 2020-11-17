# Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# hw3_3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# Python 3.8.2
# ('32bit', 'WindowsPE')

import random
from sys import getsizeof


def mem_count(mem_list):
    mem_sum = 0
    for el in mem_list:
        mem_sum += getsizeof(el)
    return mem_sum


def first_version(border_down, border_up, rand):
    random_list = [random.randint(border_down, border_up) for el in range(1, rand)]
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
    max_value = random_list[i_max]
    random_list[i_max] = random_list[i_min]
    random_list[i_min] = max_value
    sum_list = []
    sum_list.extend((border_down, border_up, rand, random_list, i,
                     max_elem, min_elem, i_max, i_min, max_value))
    return sum_list


def second_version(border_down, border_up, rand):
    random_list = [random.randint(border_down, border_up) for el in range(1, rand)]
    # print(random_list)
    max_value_ind = random_list.index(max(random_list))
    min_value_ind = random_list.index(min(random_list))
    max_value = max(random_list)
    min_value = min(random_list)
    random_list[max_value_ind] = min_value
    random_list[min_value_ind] = max_value
    sum_list = []
    sum_list.extend((border_down, border_up, rand, random_list,
                     max_value_ind, min_value_ind, max_value, min_value))
    return sum_list


def third_version(border_down, border_up, rand):
    random_list = [random.randint(border_down, border_up) for el in range(1, rand)]
    # print(random_list)
    random_list[random_list.index(max(random_list))], \
    random_list[random_list.index(min(random_list))] = random_list[random_list.index(min(random_list))], \
                                                       random_list[random_list.index(max(random_list))]
    sum_list = []
    sum_list.extend((border_down, border_up, rand, random_list))
    return sum_list


mem_list_1 = first_version(-10, 10, 10)
mem_list_2 = second_version(-10, 10, 10)
mem_list_3 = third_version(-10, 10, 10)
mem_1 = mem_count(mem_list_1)
mem_2 = mem_count(mem_list_2)
mem_3 = mem_count(mem_list_3)
print('first_version - Под переменные выделено памяти: {0}.'.format(mem_1))
print('second_version - Под переменные выделено памяти: {0}.'.format(mem_2))
print('third_version - Под переменные выделено памяти: {0}.'.format(mem_3))

# first_version - Под переменные выделено памяти: 218.
# second_version - Под переменные выделено памяти: 190.
# third_version - Под переменные выделено памяти: 134.
# Вывод: Лучший вариант - 3, т.к. он занимает меньше всего памяти, к тому же он довольно лакончиный.