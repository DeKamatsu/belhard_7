"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(num):
    if num == 2 or num == 1:
        return True
    elif num < 2:
        return False
    elif num > 2:
        return check_number(num / 2)
