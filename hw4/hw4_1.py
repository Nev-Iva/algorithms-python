# Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.

# hw3_3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
import timeit
import cProfile


def first_version(border_down, border_up, rand):
    random_list = [random.randint(border_down, border_up) for el in range(1, rand)]
    # print(random_list)
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
    # print(random_list)

# python -m timeit -n 1000 -s "import hw4_1" "hw4_1.first_version(-10, 10, 10)"
# 1000 loops, best of 5: 12.6 usec per loop
# python -m timeit -n 1000 -s "import hw4_1" "hw4_1.first_version(-10, 10, 20)"
# 1000 loops, best of 5: 24.6 usec per loop
# python -m timeit -n 1000 -s "import hw4_1" "hw4_1.first_version(-10, 10, 100)"
# 1000 loops, best of 5: 155 usec per loop
# python -m timeit -n 1000 -s "import hw4_1" "hw4_1.first_version(-10, 10, 1000)"
# 1000 loops, best of 5: 1.21 msec per loop
# cProfile.run('first_version(-10, 10, 10)')
# 53 function calls in 0.000 seconds;  1    0.000    0.000    0.000    0.000 hw4_1.py:11(first_version)
# cProfile.run('first_version(-10, 10, 100)')
# 544 function calls in 0.000 seconds; 1    0.000    0.000    0.000    0.000 hw4_1.py:11(first_version)
# cProfile.run('first_version(-10, 10, 1000)')
# 5514 function calls in 0.002 seconds; 1    0.000    0.000    0.002    0.002 hw4_1.py:11(first_version)

# Сложность алгоритма O(n).


def second_version(border_down, border_up, rand):
    random_list = [random.randint(border_down, border_up) for el in range(1, rand)]
    # print(random_list)
    max_value_ind = random_list.index(max(random_list))
    min_value_ind = random_list.index(min(random_list))
    max_value = max(random_list)
    min_value = min(random_list)
    random_list[max_value_ind] = min_value
    random_list[min_value_ind] = max_value
    # print(random_list)

# python -m timeit -n 1000 -s "import hw4_1" "hw4_1.second_version(-10, 10, 10)"
# 1000 loops, best of 5: 9.62 usec per loop
# python -m timeit -n 1000 -s "import hw4_1" "hw4_1.second_version(-10, 10, 20)"
# 1000 loops, best of 5: 19 usec per loop
# python -m timeit -n 1000 -s "import hw4_1" "hw4_1.second_version(-10, 10, 100)"
# 1000 loops, best of 5: 91 usec per loop
# python -m timeit -n 1000 -s "import hw4_1" "hw4_1.second_version(-10, 10, 1000)"
# 1000 loops, best of 5: 946 usec per loop
# cProfile.run('second_version(-10, 10, 10)')
# 57 function calls in 0.000 seconds; 1    0.000    0.000    0.000    0.000 hw4_1.py:49(second_version)
# cProfile.run('second_version(-10, 10, 100)')
# 560 function calls in 0.000 seconds;  1    0.000    0.000    0.000    0.000 hw4_1.py:49(second_version)
# cProfile.run('second_version(-10, 10, 1000)')
# 5504 function calls in 0.002 seconds; 1    0.000    0.000    0.002    0.002 hw4_1.py:49(second_version)
# Сложность алгоритма O(n).



def third_version(border_down, border_up, rand):
    random_list = [random.randint(border_down, border_up) for el in range(1, rand)]
    # print(random_list)
    random_list[random_list.index(max(random_list))], \
    random_list[random_list.index(min(random_list))] = random_list[random_list.index(min(random_list))], \
                                                       random_list[random_list.index(max(random_list))]
    # print(random_list)

# python -m timeit -n 1000 -s "import hw4_1" "hw4_1.third_version(-10, 10, 10)"
# 1000 loops, best of 5: 9.49 usec per loop
# python -m timeit -n 1000 -s "import hw4_1" "hw4_1.third_version(-10, 10, 20)"
# 1000 loops, best of 5: 27.6 usec per loop
# python -m timeit -n 1000 -s "import hw4_1" "hw4_1.third_version(-10, 10, 100)"
# 1000 loops, best of 5: 90 usec per loop
# python -m timeit -n 1000 -s "import hw4_1" "hw4_1.third_version(-10, 10, 1000)"
# 1000 loops, best of 5: 977 usec per loop
# cProfile.run('third_version(-10, 10, 10)')
# 65 function calls in 0.000 seconds; 1    0.000    0.000    0.000    0.000 hw4_1.py:78(third_version)
# cProfile.run('third_version(-10, 10, 100)')
# 564 function calls in 0.000 seconds; 1    0.000    0.000    0.000    0.000 hw4_1.py:78(third_version)
# cProfile.run('third_version(-10, 10, 1000)')
# 5566 function calls in 0.003 seconds; 1    0.000    0.000    0.003    0.003 hw4_1.py:78(third_version)
# Сложность алгоритма O(n).


# Вывод: все функции получились сложности O(n).
# Самый лучший вариант - 2 (second_version), т.к. он онаиболее быстродейственный в сравнении с двумя
# другими. Похожи данные с 3 (third_version), и в начале 2 версия даже уступает по времени, однако при
# увеличении объема данных лучше все-таки второй, а при небольших значениях разница не критична.



