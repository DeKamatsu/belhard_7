"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(num):
    if type(num) == int:
        sum = 0
        num_str = str(abs(num))
        for d in num_str:
            sum += int(d)
        return sum
    else:
        raise TypeError('Введите целое число (тип int)')


# print(sum_of_numbers(5))
# print(sum_of_numbers(25))
# print(sum_of_numbers(-25))
# print(sum_of_numbers(3255))
# print(sum_of_numbers(5.4))
