from sys import argv
from math import ceil


#                             Часы  Зп  Процент от суммы тобиш премия
# run script python3 dz1.py -v 4   1000      10

def valid_param(*args):
    res_data = []
    if len(args[0]) != 3:
        print("this is n")
        return False

    def data(d):
        for i in d:
            try:
                res_data.append(int(i))
            except Exception:
                print("this is not num")
                return False
        return res_data

    res_data = res_data if data(args[0]) else False
    return res_data


def sum_num(*args):
    time_old, zp, percent = args[0]
    print(time_old, zp, percent)
    return time_old * zp, ceil(percent / 100 * (time_old * zp))


r = valid_param(argv[2:])
if r:
    res_zp, res_prize = sum_num(r)
    print(f"Заработная плата {res_zp}; Премия {res_prize}")
