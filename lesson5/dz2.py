print(*[f"\rСтр:{k} Колл слов:{len(v.strip().split())}\n" for k, v in enumerate(open("dz2.txt", "r"), 1)])
