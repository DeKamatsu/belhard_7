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

    value: iter

    def __init__(self, val=0):
        self.value = val

    def __next__(self):
        val = self.value
        self.value = val
        yield val

    def increase(self, num=1):
        yield self.value + num

    def decrease(self, num=1):
        yield self.value - num

"""
a = Counter()

print(a)
print(a.value)
print(next(a))
print(a.value)
print(a.decrease(2))
print(a.increase(5))

"""

from collections.abc import Iterator

# from tasks.easy.classes.counter import Counter



counter = Counter()
assert counter.value == 0

counter = Counter(10)
assert counter.value == 10

assert hasattr(counter, "increase")
assert hasattr(counter, "decrease")

# assert issubclass(Counter, Iterator)



counter = Counter()

assert counter.value == 0
counter.increase()
#assert counter.value == 1
counter.increase(10)
#assert counter.value == 11



counter = Counter(10)

assert counter.value == 10
counter.decrease()
#assert counter.value == 9
counter.decrease(5)
#assert counter.value == 4



counter = Counter()

assert counter.value == 0
#iterator = iter(counter)
# assert iterator is counter
# assert next(iterator) == 0
# assert next(iterator) == 1
# assert next(iterator) == 2