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


def generate_brackets_not_working_as_well(couples):
    if type(couples) != int or couples < 0:
        raise TypeError("Введите целое положительное число")
    else:
        combo_list = list()
        current_combination = list(b for b in '(' * couples + ')' * couples)  # list of sings of one combination
        combo_list.append(combo_to_string(current_combination))  # set of string with combinations
        pick_up_index = -1
        i = 0
        b_count = 0
        can_move = True
        while i < len(current_combination) - 1:
            b_count += 1 if current_combination[i] == '(' else -1
            can_move = True if b_count > 1 else False
            if current_combination[i] == '(' and can_move:
                pick_up_index = i
            if current_combination[i] == ')' and pick_up_index >= 0:
                current_combination[pick_up_index], current_combination[i] \
                    = current_combination[i], current_combination[pick_up_index]
                combo_list.append(combo_to_string(current_combination))
                pick_up_index = -1
                can_move = False
                b_count = 0
                i = 0
            else:
                i += 1
        return combo_list


def generate_brackets(couples, s='', left=0, right=0):  # decision from internet not mine
    if type(couples) != int or couples < 0:
        raise TypeError("Введите целое положительное число")
    else:
        if left == couples and right == couples:
            print(s)
        else:
            if left < couples:
                generate_brackets(couples, s + '(', left + 1, right)
            if right < left:
                generate_brackets(couples, s + ')', left, right + 1)


#  generate_brackets(3)
