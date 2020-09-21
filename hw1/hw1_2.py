# 2. По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

def is_num(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

while True:
    x_first = (input('Введите x первой точки: '))
    y_first = (input('Введите y первой точки: '))
    x_second = (input('Введите x второй точки: '))
    y_second = (input('Введите y второй точки: '))
    if is_num(x_first) and is_num(y_first) and is_num(x_second) and is_num(y_second):
        print('Вы ввели точки: ({0}, {1}), ({2}, {3})'.format(x_first, y_first, x_second, y_second))
        x_first = float(x_first)
        x_second = float(x_second)
        y_first = float(y_first)
        y_second = float(y_second)
        k = (y_second - y_first) / (x_second - x_first)
        b = (y_second * x_first - x_second * y_first) / (x_first - x_second)
        print('y = {0} * x + {1}'.format(k, b))
        break
    else:
        print('Вы должны ввести числа.')