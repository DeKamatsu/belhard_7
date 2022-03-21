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
    f_num = 1
    f_next = 1
    while True:
        yield f_num
        f_next += f_num
        f_num = f_next - f_num
