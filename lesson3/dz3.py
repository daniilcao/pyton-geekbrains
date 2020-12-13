def task(a, b, c):
    return a + b + c - (min(a, b, c))


def validData(param):
    if len(param) == 3:
        try:
            return [int(i) for i in param]
        except Exception:
            return False
    else:
        return False


data_in = input("set free number with a space").split()
res_data = validData(data_in)
if res_data:
    print(task(*res_data))
else:
    print("invalid parameter")
