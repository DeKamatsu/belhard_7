"""
Написать генератор fibonacci, который возвращает подряд значения числе Фибоначчи

Например:

fibonacci_gen = fibonacci()

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""


def fibonacci():
    """
    генератор fibonacci возвращает подряд значения числе Фибоначчи
    """
    num_prev = 1
    f_num = 1
    while True:
        yield f_num
        f_num += num_prev
        num_prev = f_num-num_prev
