# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

comp_dict = {}
avg_sum_dict = {}
Company_income_q = namedtuple('Прибыль', ['c_first_q', 'c_second_q', 'c_third_q', 'c_fourth_q'])
count_companies = int(input('Введите количество предприятий: '))
i = 0

for i in range(count_companies):
    c_name = input('Введите название {0} компании: '.format(i+1))
    c_first_q = int(input('Введите прибыль за первый квартал: '))
    c_second_q = int(input('Введите прибыль за второй квартал: '))
    c_third_q = int(input('Введите прибыль за третий квартал: '))
    c_fourth_q = int(input('Введите прибыль за четвертый квартал: '))
    comp_dict[c_name] = Company_income_q(c_first_q=c_first_q,
                                         c_second_q=c_second_q,
                                         c_third_q=c_third_q,
                                         c_fourth_q=c_fourth_q)

print(comp_dict)

sum_list = []

for key, value in comp_dict.items():
    sum_income = sum(value)
    print('Прибыль компании {0} за год: {1}'.format(key, sum_income))
    sum_list.append(sum_income)

avg_sum = sum(sum_list) / count_companies
print('Средняя прибыль: {0}'.format(avg_sum))

for key, value in comp_dict.items():
    if sum(value) < avg_sum:
        print('Компания {0} имеет прибыль {1}, что ниже среднего {2}'.format(key, sum(value), avg_sum))
    elif sum(value) > avg_sum:
        print('Компания {0} имеет прибыль {1}, что выше среднего {2}'.format(key, sum(value), avg_sum))
    else:
        print('Компания {0} имеет прибыль {1}, что равную среднему {2}'.format(key, sum(value), avg_sum))




