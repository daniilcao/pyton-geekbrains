class Warehouse:
    def __init__(self):
        self.all_technic = []

    def set_product(self, *args):
        for k in args:
            self.all_technic.append(k.__dict__)

    def delivery(self):
        pass

class Technic:
    def __init__(self, n, c):
        self.name = n
        self.count = c


class Printer(Technic):
    def __init__(self, n, c, ct):
        super(Printer, self).__init__(n, c)
        self.cartridge_type = ct


class Scanner(Technic):
    def __init__(self, n, c, st):
        super(Scanner, self).__init__(n, c)
        self.scan_type = st


class Copier(Technic):

    def __init__(self, n, c, cs):
        super(Copier, self).__init__(n, c)
        self.cop_speed = cs


wa = Warehouse()

wa.set_product(Printer('Epson i805', 10, 'Струйный'), Scanner('Sony ps1', 5, 'Лазарный'),
               Copier('Xerox', 15, 'Очень быстрый'))
