# 6. По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

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
    first_side = input('Введите длину первой стороны: ')
    second_side = input('Введите длину второй стороны: ')
    third_side = input('Введите длину третьей стороны: ')
    if is_num(first_side) and is_num(second_side) and is_num(third_side):
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
                break
            elif first_side == second_side or first_side == third_side or second_side == third_side:
                print('Треугольник со сторонами {0}, {1}, {2} - равнобедренный.'.format(first_side, second_side, third_side))
                break
            else:
                print('Треугольник со сторонами {0}, {1}, {2} - разносторонний.'.format(first_side, second_side, third_side))
                break
        else:
            print('Такого треугольника не существует.')
            break
    else:
        print('Введите числа.')