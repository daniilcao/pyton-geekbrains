mainNum = int(input("Введите км старт: "))
day = int(input("Введите км конец: "))
r = mainNum / 100
delP = 0
inc = 1
while True:
    delP = mainNum / 100
    mainNum = mainNum + (delP * 10)
    inc += 1
    if mainNum > day:
        break

print("Результат дней {:}".format(inc))
