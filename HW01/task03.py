
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

dx = x2 - x1
if dx == 0.0:
    print('прямую нельзя описать формулой вида y = kx +b')
else:
    dy = y2 - y1
    k = dy / dx
    b = y1 - k * x1
    print(f'прямая имеет вид y = {k} * x + {b}')

