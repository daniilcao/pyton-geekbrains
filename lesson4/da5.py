from functools import reduce

items = [x for x in range(100, 1001)]
sum_all = reduce(lambda x, y: x * y, items)
print(sum_all)
