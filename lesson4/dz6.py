from itertools import count, cycle

for el in count(3):
    if el > 15:
        break
    else:
        print(el)


it = 0

for el in cycle("ABC"):
    if it > 10:
        break
    print(el)
    it += 1