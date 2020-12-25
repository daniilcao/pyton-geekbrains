class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w

    def sum_data(self, weight, thickness):
        data = self._length * self._width * weight * thickness
        print(f"{data} т")


r = Road(20, 5000)
r.sum_data(25, 5)

