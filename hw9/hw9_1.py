# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# в сумму не включаем пустую строку и строку целиком;
# без использования функций для вычисления хэша (hash(), sha1() или
# любой другой из модуля hashlib задача считается не решённой.

my_str = (input('Введите строку: '))
my_str = my_str.lower()
print('Вы ввели строку: {0}'.format(my_str))


def substring_count(ex_str):
    substring_dict = {}
    for j in range(len(ex_str)):
        str_null = ''
        for i, char in enumerate(ex_str):
            if i + j < len(ex_str):
                str_null += ex_str[i + j]
                substring_dict.update({str_null: substring_dict[str_null] + 1 if str_null in substring_dict else 1})
    len_substring = len(substring_dict) - 1
    return len_substring


sub_count = substring_count(my_str)
print('Количество различных подстрок в строке {0}: {1}'.format(my_str, sub_count))






