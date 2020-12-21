import functools
with open("dz3.txt", "r") as f_obj:
    data = f_obj.read().split()
    print(*[f"\tTop name: {data[k - 1]} sum: {v}\n" for k, v in enumerate(data) if k % 2 and int(v) > 20000],
          f"\tСреднее: {int(functools.reduce(lambda a, b: a + b, [int(v) for k, v in enumerate(data) if k % 2]) / len(data))}")
