# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена

import cProfile

NUM = 150
TESTS_NUM = 1000


def prime_numbers_cell(number, cell_len=1000):
    cell = [True] * (cell_len + 1)
    cell[0] = False
    for x in range(2, cell_len):
        if cell[x]:
            for i in range(x * 2, cell_len, x):
                cell[i] = False

    prime_numbers = [x for x in range(cell_len) if cell[x]]
    return prime_numbers[number]


def prime_numbers_wo_cell(number):
    prime_numbers = [2]
    x = 3
    while len(prime_numbers) < number:
        is_prime_number = True
        for prime_number in prime_numbers:
            if x % prime_number == 0:
                is_prime_number = False
                break
        if is_prime_number:
            prime_numbers.append(x)
        x += 2
    return prime_numbers[-1]


def test_1():
    for i in range(TESTS_NUM):
        prime_numbers_cell(NUM)


def test_2():
    for i in range(TESTS_NUM):
        prime_numbers_wo_cell(NUM)


print(f'ТЕСТ_1. {TESTS_NUM} раз ищем {NUM}-ое простое число с помощью решета Эратосфена')
cProfile.run('test_1()')
print(f'ТЕСТ_2. {TESTS_NUM} раз ищем {NUM}-ое простое число другим способом')
cProfile.run('test_2()')
print(f'Проверка: {NUM}-ое простое число, найденное методом решета Эратосфена, -- '
      f'{prime_numbers_cell(NUM)}'
      f', и без него -- '
      f'{prime_numbers_wo_cell(NUM)}'
      )
#
# ТЕСТ_1. 10000 раз ищем 150-ое простое число с помощью решета Эратосфена
#          20004 function calls in 1.197 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.197    1.197 <string>:1(<module>)
#     10000    0.946    0.000    1.181    0.000 task2.py:11(prime_numbers_cell)
#     10000    0.235    0.000    0.235    0.000 task2.py:19(<listcomp>)
#         1    0.016    0.016    1.197    1.197 task2.py:38(test_1)
#         1    0.000    0.000    1.197    1.197 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# ТЕСТ_2. 10000 раз ищем 150-ое простое число другим способом
#          5820004 function calls in 4.398 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    4.397    4.397 <string>:1(<module>)
#     10000    4.049    0.000    4.391    0.000 task2.py:23(prime_numbers_wo_cell)
#         1    0.007    0.007    4.397    4.397 task2.py:43(test_2)
#         1    0.000    0.000    4.398    4.398 {built-in method builtins.exec}
#   4320000    0.241    0.000    0.241    0.000 {built-in method builtins.len}
#   1490000    0.101    0.000    0.101    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# Проверка: 150-ое простое число, найденное методом решета Эратосфена, -- 863, и без него -- 863
#

