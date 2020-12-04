import time

i = input("Введите ваше цыфру: ")
r = -1
while i > 10:
    d = i % 10  # Получаем остаток
    i = i // 10  # Отбрасывая дробную часть
    if d > r:
        r = d

print("Top num %s" % r)
