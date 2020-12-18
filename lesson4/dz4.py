my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
seen = []
[seen.append(x) for x in my_list if x not in seen]
print(seen)
