class Data:
    def __init__(self, d):
        Data.data = d

    @classmethod
    def parse_data(cls):
        return [int(x) for x in cls.data.split('.')]

    @staticmethod
    def valid_data(obj):
        data = obj.parse_data()
        if data[0] > 31 or data[0] < 1:
            print("ошибка день месяц")
        if data[1] > 12 or data[1] < 1:
            print("ошибка месяц")
        if data[2] == 0:
            print("ошибка год")
        return "Ok data"


d = Data("13.9.2020")
print(*d.parse_data())
print(d.valid_data(d))
