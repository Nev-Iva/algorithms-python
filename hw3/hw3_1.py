# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

num_list = [el for el in range(2, 100)]
div_list = [el for el in range(2, 10)]
result_dict = {}
for elem in div_list:
    result_dict[elem] = []
    for el in num_list:
        if el % elem == 0:
            result_dict[elem].append(el)

for key, value in result_dict.items():
    print('Кратны {0} - {1} чисел'.format(key, len(value)))