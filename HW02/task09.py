# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def getsum(number):
    result = 0
    for i in number:
        result += int(i)
    return result


user_input = input(f'Введите последовательность цифр: ')
numbers = user_input.split()

max_number = numbers[0]
max_value = getsum(max_number)

for number in numbers:
    calc = getsum(number)
    if calc > max_value:
        max_value = calc
        max_number = number

print(f'наибольшее по сумме цифр: {max_number}, с суммой чисел: {max_value}')
