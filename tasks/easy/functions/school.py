"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(school_list: dict, class_: str):
    try:
        school_list[class_] += 1
    except "Проблема с форматом данных 'список классов - класс'" as ex:
        return ex


def decr_students(school_list: dict, class_: str):
    try:
        school_list[class_] -= 1 if school_list[class_] > 0 else school_list[class_]
    except "Проблема с форматом данных 'список классов - класс'" as ex:
        return ex


def add_class(school_list: dict, class_: str):
    school_list[class_] = 0


def remove_class(school_list: dict, class_: str):
    if class_ in school_list:
        school_list.pop(class_)


def calc_students(school_list: dict):
    return len(school_list)
