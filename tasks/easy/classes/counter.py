class Counter:
    """
    Описать класс Counter, реализующий целочисленный счетчик.
    который может увеличивать или уменьшать свое значение (атрибут value)
    на единицу в заданном диапазоне.

    Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

    Определить атрибуты:

    - value - текущее значение счетчика

    Определить методы:

    - инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
    - increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
    - decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
    - метод __iter__
    - метод __next__
    """

    value: int

    def __init__(self, val=0):
        self.value = val

    def __iter__(self):
        return self

    def __next__(self):
        val = self.value
        self.value += 1
        return val

    def increase(self, num=1):
        val = self.value
        self.value += num
        return val

    def decrease(self, num=1):
        val = self.value
        self.value -= num
        return val
