class Cell:
    def __init__(self, cell):
        self.call_cell = int(cell)

    def __str__(self):
        return f'клетки {self.call_cell}'

    def __add__(self, other):
        return Cell(self.call_cell + other.call_cell)

    def __sub__(self, other):
        return Cell(self.call_cell - other.call_cell) if (self.call_cell - other.call_cell) > 0 else 'меньше нуля'

    def __mul__(self, other):
        return Cell(self.call_cell * other.call_cell)

    def __truediv__(self, other):
        return Cell(self.call_cell / other.call_cell) if self.call_cell > 0 and other.call_cell > 0 else 'меньше нуля'

    def make_order(self, n):
        row = ''
        for i in range(int(self.call_cell / n)):
            row += f'{"*" * n} \\n'
        row += f'{"*" * (self.call_cell % n)}'
        return row


c1 = Cell(30)
c2 = Cell(20)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1.make_order(15))
print(c2.make_order(5))
