# 4. Определить, какое число в массиве встречается чаще всего.

import random

random_list = [random.randint(0, 20) for el in range(1, 20)]
max_count_num = random_list[0]
max_count = 1
print(random_list)

for i in range(len(random_list) - 1):
    count = 1
    for k in range(i + 1, len(random_list)):
        if random_list[i] == random_list[k]:
            count += 1
    if count > max_count:
        max_count = count
        max_count_num = random_list[i]

if max_count > 1:
    print('Больше всего встречается число {0} - {1} раз.'.format(max_count_num, max_count))
else:
    print('Повторений нет.')

