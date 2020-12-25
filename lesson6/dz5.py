class Stationery:
    def __init__(self, name):
        self.title = name

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title} пишет буквы")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} друг художника")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title} подумал он")


p = Pen("Ручка")
p.draw()

p = Pencil("Карандаш")
p.draw()

p = Handle("Ручка")
p.draw()
