
year = abs(int(input('Укажите год: ')))

check_1 = year % 4 == 0
check_2 = year % 100 == 0
check_3 = year % 400 == 0
isLeapYear = (check_1 and not check_2) or check_3

if isLeapYear:
    print(f'Это високосный год')
else:
    print(f'Это не високосный год')
