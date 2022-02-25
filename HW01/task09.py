

x1 = float(input('x1 = '))
x2 = float(input('x2 = '))
x3 = float(input('x3 = '))

c12 = x1 < x2
c13 = x1 < x3
c21 = x2 < x1
c23 = x2 < x3
c31 = x3 < x1
c32 = x3 < x2

is_x1_middle = c12 != c13
is_x2_middle = c21 != c23
is_x3_middle = c31 != c32

if is_x1_middle:
    print(f'1-ое введенное число {x1} является "средним"')

if is_x2_middle:
    print(f'2-ое введенное число {x2} является "средним"')

if is_x3_middle:
    print(f'3-ое введенное число {x3} является "средним"')



#
# print(f'c12 = x1 < x2 : {c12}')
# print(f'c13 = x1 < x3 : {c13}')
# print(f'c21 = x2 < x1 : {c21}')
# print(f'c23 = x2 < x3 : {c23}')
# print(f'c31 = x3 < x1 : {c31}')
# print(f'c32 = x3 < x2 : {c32}')
#
