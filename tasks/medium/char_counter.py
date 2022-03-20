"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
STR_VAL = 'python is the fastest-growing major programming languagez'


def count_char(str_val: str):
    char_list = {}
    count = 0
    for i in str_val[count:]:
        char_list[i] = str_val.count(i)
        count += 1
    return char_list

