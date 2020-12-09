listDat = []
listSec = []
while True:
    setParam = input("Write:")
    listSec.append(setParam)
    listDat.append(setParam)
    ledList = len(listSec) % 2
    if ledList == 0:
        v1, v2 = listSec
        listDat.remove(v1)
        listDat.remove(v2)
        listDat.extend([v2, v1])
        listSec.clear()
    print(listDat)
