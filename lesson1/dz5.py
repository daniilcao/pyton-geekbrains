revenue = int(input("Введите прибыль: "))
costProduct = int(input("Введите издержки: "))

profit = revenue - costProduct


if revenue < costProduct:
    print("Убыток компании: %s" % profit)
else:
    print("Прибыль компании: %s" % profit)

workers = int(input("Введите численность сотрудников: "))
resProfitWorkers = profit / workers

if resProfitWorkers > 0:
    print("Прибыль расчете на одного сотрудника: {:.0f}".format(resProfitWorkers))
else:
    print("Убыто расчете на одного сотрудника: {:.0f}".format(resProfitWorkers))
