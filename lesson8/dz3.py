class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


arr = []
while True:
    try:
        param = input("Ведите число: ")
        if param == "stop":
            print(arr)
            break
        param = int(param)
    except ValueError:
        print(OwnError("Это не число"))
    else:
        arr.append(param)
