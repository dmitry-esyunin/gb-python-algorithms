
num = int(input('Введите число:'))
ones = num % 10
tens = num % 100 // 10
hundreds = num // 100
sum = ones + tens + hundreds
multi = ones * tens * hundreds
print(f'Сумма:\t{sum}\nПроизведение:\t{multi}')

