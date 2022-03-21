"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(num):
    """
    генератор fibonacci возвращает подряд значения чисел Фибоначчи до num
    """
    if num <= 1:
        raise ValueError('Введите значение больше 1')
    else:
        num_prev = 0
        f_num = 1
        while f_num <= num:
            yield f_num
            f_num += num_prev
            num_prev = f_num - num_prev


# print(next(fibonacci(0)))
# for i in fibonacci(15):
#     print(i)
