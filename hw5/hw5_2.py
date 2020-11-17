# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

dict_16 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
           0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
           10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def list_to_str(my_list):
    my_str = ''
    for el in my_list:
        my_str += el
    return my_str


first_num = list(input('Введите первое число: ').upper())
second_num = list(input('Введите второе число число: ').upper())
f_num = first_num
s_num = second_num
mfirst_num = first_num
msecond_num = second_num
sum_list = deque()
meter = 0

if len(s_num) > len(f_num):
    f_num, s_num = deque(s_num), deque(f_num)
else:
    f_num, s_num = deque(f_num), deque(s_num)
while f_num:
    if s_num:
        res = dict_16[f_num.pop()] + dict_16[s_num.pop()] + meter
    else:
        res = dict_16[f_num.pop()] + meter
    meter = 0
    if res < 16:
        sum_list.appendleft(dict_16[res])
    else:
        sum_list.appendleft(dict_16[res - 16])
        meter = 1
if meter:
    sum_list.appendleft('1')
sum_str = list_to_str(list(sum_list))
print('Сумма чисел: {0} + {1} = {2}'.format(first_num[0], second_num[0], sum_str))

multi_list = deque()
mm_list = deque([deque() for el in range(len(second_num))])
first_num, second_num = first_num.copy(), deque(second_num)
for i in range(len(second_num)):
    m = dict_16[second_num.pop()]
    for j in range(len(first_num) - 1, -1, -1):
        mm_list[i].appendleft(m * dict_16[first_num[j]])
    for el in range(i):
        mm_list[i].append(0)
transfer = 0
for k in range(len(mm_list[-1])):
    res = transfer
    for i in range(len(mm_list)):
        if mm_list[i]:
            res += mm_list[i].pop()
    if res < 16:
        multi_list.appendleft(dict_16[res])
    else:
        multi_list.appendleft(dict_16[res % 16])
        transfer = res // 16
if transfer:
        multi_list.appendleft(dict_16[transfer])

multi_str = list_to_str(list(multi_list))
print('Произведение чисел: {0} * {1} = {2}'.format(mfirst_num[0], msecond_num[0], multi_str))




