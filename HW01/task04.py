import random

i0 = int(input('Генерация случайного целого числа. Укажите нижнюю границу = '))
i1 = int(input('Генерация случайного целого числа. Укажите верхнюю границу = '))
i = random.randint(i0, i1)
print(i)


f0 = float(input('Генерация случайного вещественного числа. Укажите нижнюю границу = '))
f1 = float(input('Генерация случайного вещественного числа. Укажите верхнюю границу = '))
f = random.uniform(f0, f1)
print(f)


s0 = input('Генерация случайного символа. Укажите нижнюю границу = ').lower()
s1 = input('Генерация случайного символа. Укажите верхнюю границу = ').lower()
x0 = ord(s0)
x1 = ord(s1)
x = random.randint(x0, x1)
s = chr(x)
print(s)