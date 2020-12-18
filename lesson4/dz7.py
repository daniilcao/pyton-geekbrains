
def fact(n):
    it = 1
    for el in range(1,n+1):
        it *= el
        yield f'{el}! = {it}'


for el in fact(4):
    print(el)


