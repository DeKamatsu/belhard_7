"""
Написать функцию hello, которая принимает аргумент name - строку с именем и
выводит принтом "Привет, {name}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""


def log_decorator(func):
    def comment_func(*args, **kwargs):
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        func(*args, **kwargs)
        print(f"Выполнено {func.__name__}")
    return comment_func


@log_decorator
def hello(name):
    print(f"Привет, {name}")


# def linear_builder(k, b):
#     def helper(x):
#         return k * x + b
#     return helper
#
# linf = linear_builder(3, 9)
#
#
# @linear_builder(3, 9)  # предпосылка для декорирования, но почему не получается?
# def linf(x):
#     print(linear_builder(k=3, b=9))
#
# linf(6)

