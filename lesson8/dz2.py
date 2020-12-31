class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    res = 100/0
except ZeroDivisionError:
    print(OwnError("На ноль делить нельзя"))
