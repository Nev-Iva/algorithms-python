# На улице встретились N друзей.
# Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было? Примечание.
# Решите задачу при помощи построения графа.

n_count = int(input('Введите количество друзей: '))


def count_handshakes(n_count):
    f_set = set()
    for el in range(n_count):
        for elem in range(n_count):
            if el != elem:
                s_set = set()
                s_set.add(el)
                s_set.add(elem)
                f_set.add(tuple(s_set))
    # print(f_set)
    return len(f_set)


print('Количество рукопожатий среди {0} друзей: {1}.'.format(n_count, count_handshakes(n_count)))


