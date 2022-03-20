"""
Написать рекурсивную функцию  line_print, которая принимает 1 аргумент - список

Функция печатает каждых элемент на новой строке.

Если элемент списка - список, то его элементы должны выводиться с отступом
относительно родительского на 4 пробела

Например:

some_list = [1, 2, [1, 2, [5, 7], 3], 8]

line_print(some_list)
1
2
    1
    2
        5
        7
    3
8
"""


def line_print(list_to_print, lvl=0):
    i = 0
    while i < len(list_to_print):
        if type(list_to_print[i]) == list:
            line_print(list_to_print[i], lvl + 1)
        else:
            print('    '*lvl + str(list_to_print[i]))
        i += 1


# some_list = [1, 2, [1, 2, [5, 7], 3], 8]
# line_print(some_list)
