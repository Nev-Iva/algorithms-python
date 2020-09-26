# 6. По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.


first_side = input('Введите длину первой стороны: ')
second_side = input('Введите длину второй стороны: ')
third_side = input('Введите длину третьей стороны: ')
if first_side.isdigit() and second_side.isdigit() and third_side.isdigit():
    first_side = float(first_side)
    second_side = float(second_side)
    third_side = float(third_side)
    sum_1_2 = first_side + second_side
    sum_2_3 = second_side + third_side
    sum_3_1 = third_side + first_side
    if (third_side < sum_1_2) and (first_side < sum_2_3) and (second_side < sum_3_1):
        print('Треугольник существует.')
        if first_side == second_side == third_side:
            print('Треугольник со сторонами {0}, {1}, {2} - равносторонний.'.format(first_side, second_side, third_side))
        elif first_side == second_side or first_side == third_side or second_side == third_side:
            print('Треугольник со сторонами {0}, {1}, {2} - равнобедренный.'.format(first_side, second_side, third_side))
        else:
            print('Треугольник со сторонами {0}, {1}, {2} - разносторонний.'.format(first_side, second_side, third_side))

    else:
        print('Такого треугольника не существует.')
else:
    print('Введенные данные не являются числами.')