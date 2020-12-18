param = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def help_f(index, num, param):
    if index != 0:
        res = param[index - 1]
        num = num if res < num else False
        return num
    return False


new_list = [el for index, el in enumerate(param) if help_f(index, el, param)]
print(new_list)
