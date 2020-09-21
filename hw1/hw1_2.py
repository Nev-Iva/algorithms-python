# 2. По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

x_first = (input('Введите x первой точки: '))
y_first = (input('Введите y первой точки: '))
x_second = (input('Введите x второй точки: '))
y_second = (input('Введите y второй точки: '))
if x_first.isdigit() and y_first.isdigit() and x_second.isdigit() and y_second.isdigit():
    print('Вы ввели точки: ({0}, {1}), ({2}, {3})'.format(x_first, y_first, x_second, y_second))
    x_first = int(x_first)
    x_second = int(x_second)
    y_first = int(y_first)
    y_second = int(y_second)
    k = (y_second - y_first) / (x_second - x_first)
    b = (y_second * x_first - x_second * y_first) / (x_first - x_second)
    print('y = {0} * x + {1}'.format(k, b))
else:
    print('Вы должны ввести числа.')