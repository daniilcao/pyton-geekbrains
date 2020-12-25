from tkinter import Canvas, Tk, Label
import time


class TrafficLight:
    def __init__(self, color):
        self.__c = color

    def ball(self, c, color, x, y):
        b = c.create_oval(0, 0, 100, 100, fill=color)
        c.move(b, x, y)

    def running(self):
        c = Canvas(root, width=110, height=350, bg="black")
        c.pack()
        p = [5, 110, 220]
        [self.ball(c, "#808080", 5, k) for k in p]
        it = 0
        while True:
            param = self.__c[it]
            b = c.create_oval(0, 0, 100, 100, fill=list(param.keys())[0])
            c.move(b, 5, p[it])
            root.update()
            time.sleep(sum(param.values()))
            c.delete(b)
            it = (it + 1) if it < 2 else 0


root = Tk()
tra = TrafficLight([{'red': 2}, {'yellow': 5}, {'green': 5}])
tra.running()
root.mainloop()
