# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.
import cProfile

TESTS_NUM = 100000
array = [1, 2, 4, 8, 16, 32, 64, 128, 256]


def method_one():
    return sum(array) - min(array) - max(array)


def method_two():
    min_value = array[0]
    max_value = array[0]
    res = 0
    for item in array:
        if item < min_value:
            min_value = item
        if item > max_value:
            max_value = item
        res += item

    return res - min_value - max_value


def test_1():
    for _ in range(TESTS_NUM):
        method_one()


def test_2():
    for _ in range(TESTS_NUM):
        sum_ = sum(array) - min(array) - max(array)


print(f'ТЕСТ_1.')
cProfile.run('test_1()')
print(f'ТЕСТ_2.')
cProfile.run('test_2()')

print(method_one())
print(method_two())

#
# ТЕСТ_1.
#          400004 function calls in 0.226 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.226    0.226 <string>:1(<module>)
#         1    0.027    0.027    0.226    0.226 task1.py:26(test_1)
#    100000    0.075    0.000    0.200    0.000 task1.py:8(method_one)
#         1    0.000    0.000    0.226    0.226 {built-in method builtins.exec}
#    100000    0.046    0.000    0.046    0.000 {built-in method builtins.max}
#    100000    0.047    0.000    0.047    0.000 {built-in method builtins.min}
#    100000    0.032    0.000    0.032    0.000 {built-in method builtins.sum}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# ТЕСТ_2.
#          300004 function calls in 0.177 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.177    0.177 <string>:1(<module>)
#         1    0.069    0.069    0.177    0.177 task1.py:32(test_2)
#         1    0.000    0.000    0.177    0.177 {built-in method builtins.exec}
#    100000    0.040    0.000    0.040    0.000 {built-in method builtins.max}
#    100000    0.041    0.000    0.041    0.000 {built-in method builtins.min}
#    100000    0.028    0.000    0.028    0.000 {built-in method builtins.sum}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
