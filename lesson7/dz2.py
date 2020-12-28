from math import ceil


class Clothes:
    def __init__(self, size, height, n):
        self.name = n
        self.size = size
        self.height = height

    @property
    def get_all_cloth(self):
        return f'Площадь общий  ткани {self.name} {ceil(self.size / 6.5 + 0.5) + ceil(self.height * 2 + 0.3)}'

    def __add__(self, other):
        return f'Площадь общий ткани {self.name} и {other.name} {(ceil(self.size / 6.5 + 0.5) + ceil(self.height * 2 + 0.3)) + (ceil(other.size / 6.5 + 0.5) + ceil(other.height * 2 + 0.3))}'


class Coat(Clothes):
    def __init__(self, s, h):
        super().__init__(s, h, 'пальто')
        self.__name = "пальто"

    def __str__(self):
        return f'Площадь ткани размера {self.name} {ceil(self.size / 6.5 + 0.5)}'


class Jacket(Clothes):
    def __init__(self, s, h):
        super().__init__(s, h, 'костюм')

    def __str__(self):
        return f'Площадь ткани роста {self.name} {ceil(self.height * 2 + 0.3)}'


c = Coat(20, 67)
j = Jacket(2, 8)

print(c.get_all_cloth)
print(j.get_all_cloth)
print("-----")
print(c)
print(j)
print("-----")
print(c + j)
