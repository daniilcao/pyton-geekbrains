import functools

f = open("dz5.txt", "w")
print(f"Набор чисел {' '.join([str(k) for k in range(1, 20)])}",
      f"Сумма {functools.reduce(lambda a, b: a + b, [k for k in range(1, 20)])}", file=f, sep='\n')
f.close()
