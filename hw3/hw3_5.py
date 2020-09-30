# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

random_list = [random.randint(-20, 20) for el in range(1, 15)]
count = -1
i = 0
print(random_list)

while i < len(random_list):
    if random_list[i] < 0 and count == -1:
        count = i
    elif random_list[i] < 0 and random_list[i] > random_list[count]:
        count = i
    i += 1

print('Макс. отрицательный элемент {0} находится на позиции {1} (нумерация с 0)'.format(random_list[count], count))










