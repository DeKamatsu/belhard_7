"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(int_list):
    int_set = set()
    for num in int_list:
        if num in int_set:
            print('Yes')
        else:
            print('No')
        int_set.add(num)


# yes_or_no((1, 3, 4, 12, 0, 5, 1, 4, 3, '1', '1'))
