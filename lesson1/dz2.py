time = int(input("введите секунды: "))
minn = time / 60
hr = minn / 60

rHr = int(hr)
rMin = int(minn - (int(hr)*60))
rSec = time - ((rHr * 60) * 60) - (rMin * 60)

if rHr < 10:
    rHr = "0" + str(rHr)
if rMin < 10:
    rMin = "0" + str(rMin)
if rSec < 10:
    rSec = "0" + str(rSec)

print("%s:%s:%s" % (rHr, rMin,rSec))

