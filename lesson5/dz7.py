import functools
import json

with open("dz7.txt", "r") as f_obj:
    data_param = f_obj.read()
    data_param = [k.split(" ") for k in data_param.split("\n")]
    data_res = []
    for k in data_param:
        if int(k[2]) > int(k[3]):
            data_res.append({k.pop(0): int(k[1])})
        else:
            data_res.append({k.pop(0): "Убыток"})

    p = [list(v.values())[0] for k, v in enumerate(data_res)]
    data_res.append({"average": int(
        functools.reduce(lambda a, b: a + b, [k for k in p if k != "Убыток"]) / len([k for k in p if k != "Убыток"]))})
    write_file = open("dz7.json", "w")
    json.dump(data_res, write_file, ensure_ascii=False)
    write_file.close()
    print(data_res)
