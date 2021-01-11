# Закодируйте любую строку по алгоритму Хаффмана.
import heapq
from collections import Counter
from collections import namedtuple

my_str = input('Введите строку: ')


class Node(namedtuple("Node", ["left", "right"])):
    def bypass(self, code, acc):
        self.left.bypass(code, acc + "0")
        self.right.bypass(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def bypass(self, code, acc):
        code[self.char] = acc or "0"


def encode_func(ex_str):
    ex_list = []
    for ch, freq in Counter(ex_str).items():
        ex_list.append((freq, len(ex_list), Leaf(ch)))
    heapq.heapify(ex_list)
    count = len(ex_list)
    while len(ex_list) > 1:
        freq1, _count1, left = heapq.heappop(ex_list)
        freq2, _count2, right = heapq.heappop(ex_list)
        heapq.heappush(ex_list, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if ex_list:
        [(_freq, _count, root)] = ex_list
        root.bypass(code, "")
    return code


def decode_func(encoded, code):
    ex_list =[]
    null_str = ""
    for el in encoded:
        null_str += el
        for dec_ch in code:
            if code.get(dec_ch) == null_str:
                ex_list.append(dec_ch)
                null_str = ""
                break
    return "".join(ex_list)


def start_func(ex_str):
    code = encode_func(ex_str)
    encoded = "".join(code[ch] for ch in ex_str)
    # print(len(code), len(encoded))
    # for ch in sorted(code):
        # print("{}: {}".format(ch, code[ch]))
    print('Закодированная строка: {0}'.format(encoded))
    decoded = decode_func(encoded, code)
    print('После обратного декодирования получилась строка: {0}'.format(decoded))


start_func(my_str)
