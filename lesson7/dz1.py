class Matrix:
    def __init__(self, *args):
        self.m = args

    def __str__(self):
        z = list(zip(*self.m))
        resS = ''
        for x in z:
            for xx in x:
                resS += f'{xx} '
            resS += '\n'
        return resS

    def __add__(self, other):
        resM = []
        for k in range(len(self.m)):
            con = 0
            for kk in range(len(self.m[k])):
                con += self.m[k][kk] + other.m[k][kk]

            resM.append(con)
        return resM


m1 = Matrix([1, 2, 30, 4, 5], [5, 50, 3, 2, 1], [5, 4, 3, 2, 12])
print(m1)
m2 = Matrix([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1])
print(m1 + m2)

