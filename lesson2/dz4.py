strName = input("set string separated by a space:")
reList = strName.split()
for k in range(len(reList)):
    s = reList[k]
    if len(s) > 10:
        s = s[:9]
    print(f"{k}:{s}")
