
a = abs(float(input('Укажите длину первого отрезка (>0): ')))
b = abs(float(input('Укажите длину второго отрезка (>0): ')))
c = abs(float(input('Укажите длину третьего отрезка (>0): ')))

check_1 = a + b >= c
check_2 = a + c >= b
check_3 = b + c >= a
isTriangle = check_1 and check_2 and check_3
isEquilateral = (a == b) and (a == c)
isIsosceles = not isEquilateral and ((a == b) or (b == c) or (a == c))
isAnotherTriangle = not isEquilateral and not isIsosceles

if isTriangle:
    if isEquilateral:
        print(f'Это равнестронний треугольник')

    if isIsosceles:
        print(f'Это равнобедренный треугольник')

    if isAnotherTriangle:
        print(f'Это разносторонний треугольник')
else:
    print(f'Это не треугольник')
