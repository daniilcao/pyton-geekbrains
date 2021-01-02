class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        r = self.b + other.b
        return f'{self.a + other.a} {r if (r < 0) else f"+{r}"}i'

    def __mul__(self, other):
        a = (other.a * self.a)
        ai = (other.a * self.b)

        pi = (other.b * self.a)
        p = ((other.b * self.b)*-1)
        r = ai + pi
        return f'{a+p} {r if (r < 0) else f"+{r}"}i'

    def __str__(self):
        return f'{self.a} + {self.b}i'

# z_1 = Complex(1, -3)
# z_2 = Complex(2, 5)
z_1 = Complex(5, 2)
z_2 = Complex(3, 7)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
