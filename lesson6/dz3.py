class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self._position = position


class Position(Worker):
    def get_full_name(self):
        print(f"Name:{self.name}")

    def get_total_income(self):
        print(self._position.get('wage') + self._position.get('bonus'))


p = Position("Daniil", "Zabota", {"wage": 10000, "bonus": 3000})
p.get_full_name()
p.get_total_income()
