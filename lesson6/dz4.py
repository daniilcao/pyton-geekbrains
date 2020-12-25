class Car:
    def __init__(self, s, c, n, b):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = b

    def show_speed(self):
        print(f"Car {self.name} speed {self.speed}")

    def go(self):
        print(f"Car {self.name} go go go")

    def stop(self):
        print(f"Car {self.name} stop")
        pass

    def turn(self, p):
        print(f"Car {self.name} {p}")
        pass


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} high speed")
            return
        print(f"Car {self.name} speed {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} high speed")
            return
        print(f"Car {self.name} speed {self.speed}")
    pass


class PoliceCar(Car):
    pass


t = TownCar(60, "red", "Газель", False)
t.go()
t.show_speed()
t.stop()
t.turn("left")


t = WorkCar(60, "red", "MAZ", False)
t.go()
t.show_speed()
t.stop()
t.turn("left")

