def sum_my(x, y):
    res_d = x
    for k in range(1, y):
        res_d = res_d * x
    return res_d


def validData(param):
    if len(param) == 2:
        try:
            return [int(i) for i in param]
        except Exception:
            return False
    else:
        return False


data_in = input("set two number with a space").split()
res_data = validData(data_in)
if res_data:
    print(sum_my(*res_data))
else:
    print("invalid parameter")
