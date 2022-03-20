"""
Задача из собеседования в яндекс

Написать рекурсивную функцию generate_brackets, которая принимает длину -
количество пар скобок, и будет генерировать все возможные варианты
скобочных последовательностей


Например:
generate_brackets(3)
n = 3
((()))
(()())
(())()
()(())
()()()

n = 4
(((())))
((()()))
((())())
((()))()
(()(()))
(()()())
(()())()
(())(())
(())()()
()((()))
()(()())
()(())()
()()(())
()()()()
"""


def combo_to_string(combo):
    return ''.join([str(b) for b in combo])


def generate_brackets(couples):
    if type(couples) != int or couples < 1:
        raise TypeError("Введите целое положительное число")
    else:
        combo_list = list()
        current_combination = list(b for b in '(' * couples + ')' * couples)  # list of sings of one combination
        combo_list.append(combo_to_string(current_combination))  # set of string with combinations
        pick_up_index = -1
        i = 1
        while i < len(current_combination)-1:
            if current_combination[i] == '(':
                pick_up_index = i
            if current_combination[i] == ')' and pick_up_index >= 0:
                current_combination[pick_up_index], current_combination[i] \
                    = current_combination[i], current_combination[pick_up_index]
                combo_list.append(combo_to_string(current_combination))
                pick_up_index = -1
                i = 1
            else:
                i += 1
        return combo_list


print(generate_brackets(5))

