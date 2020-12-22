import re
import functools

with open("dz6.txt", "r") as f_obj:
    res_data = re.sub(r"(\([\w]*\))", "", f_obj.read())
    res_data = re.sub(r"[—,.,:]", "", res_data)
    res_data = res_data.split('\n')
    res_data = [k.split(" ") for k in res_data]
    data = {}
    for v in res_data:
        name = v.pop(0)
        data[name] = functools.reduce(lambda a, b: a + b, [int(c) for c in v if c != ""])
    print(data)

