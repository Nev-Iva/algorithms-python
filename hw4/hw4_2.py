# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход
# натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

import cProfile


# Первый — с помощью алгоритма «Решето Эратосфена».
def first_erat(index):
    sieve = [i for i in range(index + 1)]
    sieve[1] = 0
    for el in range(2, index + 1):
        if sieve[el] != 0:
            elem = el * 2
            while elem <= index:
                sieve[elem] = 0
                elem += el
    nums = [el for el in sieve if el != 0]
    return nums[-1]
    # print('Простое число: '.format(nums[-1]))


# python -m timeit -n 1000 -s "import hw4_2" "hw4_2.first_erat(10)"
# 1000 loops, best of 5: 8.59 usec per loop
# python -m timeit -n 1000 -s "import hw4_2" "hw4_2.first_erat(20)"
# 1000 loops, best of 5: 10 usec per loop
# python -m timeit -n 1000 -s "import hw4_2" "hw4_2.first_erat(100)"
# 1000 loops, best of 5: 28.7 usec per loop
# python -m timeit -n 1000 -s "import hw4_2" "hw4_2.first_erat(1000)"
# 1000 loops, best of 5: 375 usec per loop

# cProfile.run('first_erat(1000)')
# Для 10: 1    0.000    0.000    0.000    0.000 hw4_2.py:9(first_erat)
# Для 100: 1    0.000    0.000    0.000    0.000 hw4_2.py:9(first_erat)
# Для 1000: 1    0.001    0.001    0.001    0.001 hw4_2.py:9(first_erat)

# Сложность алгоритма O(n).

# Второй — без использования «Решета Эратосфена».
def second_my(index):
    i = 1
    number = 1
    nums = [2]
    if index == 1:
        return 2
    while i != index:
        number += 2
        for num in nums:
            if number % num == 0:
                break
        else:
            i += 1
            nums.append(number)
    return number

# python -m timeit -n 1000 -s "import hw4_2" "hw4_2.second_my(10)"
# 1000 loops, best of 5: 7.32 usec per loop
# python -m timeit -n 1000 -s "import hw4_2" "hw4_2.second_my(20)"
# 1000 loops, best of 5: 17.9 usec per loop
# python -m timeit -n 1000 -s "import hw4_2" "hw4_2.second_my(100)"
# 1000 loops, best of 5: 331 usec per loop
# python -m timeit -n 1000 -s "import hw4_2" "hw4_2.second_my(1000)"
# 1000 loops, best of 5: 31 msec per loop

# cProfile.run('second_my(1000)')
# Для 10: 1    0.000    0.000    0.000    0.000 hw4_2.py:38(second_my)
# Для 100: 1    0.001    0.001    0.001    0.001 hw4_2.py:38(second_my)
# Для 1000: 1    0.077    0.077    0.077    0.077 hw4_2.py:38(second_my)

# Сложность алгоритма O(n).


# Вывод: с увеличением объема данных алгоритм «Решето Эратосфена» работает быстрее второго.
