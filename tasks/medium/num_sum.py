"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(num):
    if type(num) == int:
        q = 0
        num_str = str(abs(num))
        for d in num_str:
            q += int(d)
        return q
    else:
        raise TypeError('Введите целое число (тип int)')


# print(sum_of_numbers(5))
# print(sum_of_numbers(25))
# print(sum_of_numbers(-25))
# print(sum_of_numbers(3255))
# print(sum_of_numbers(5.4))
