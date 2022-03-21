"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").
Проверить, что все аргументы целые можно с помощью функции all:
https://pyneng.readthedocs.io/ru/latest/book/10_useful_functions/all_any.html

Если все аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args, **kwargs):
    args_sum = 0
    for a in args:
        if type(a) == dict:
            if all(str(a[key]).isalpha() for key in a):
                kwargs_max_len = max(len(a[key]) for key in a)
            else:
                raise TypeError("Все аргументы - ключевые слова должны быть строками")
    if all(type(num) == int for num in args):
        args_sum = sum(num for num in args)
    else:
        raise TypeError("Все позиционные аргументы должны быть целыми")
    if kwargs:
        if all(str(kwargs[key]).isalpha() for key in kwargs):
            kwargs_max_len = max(len(kwargs[key]) for key in kwargs)
        else:
            raise TypeError("Все аргументы - ключевые слова должны быть строками")
    return {"args_sum": args_sum, "kwargs_max_len": kwargs_max_len}


# print(dict_from_args([1, 2], {"a": "aa", "b": "bbb"}))
# print(dict_from_args([1, "2"], {"a": "aa", "b": "bbb"}))
# print(dict_from_args([1, 2], {"a": 2, "b": "bbb"}))
