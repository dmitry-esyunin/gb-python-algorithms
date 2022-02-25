# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые
# данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
# снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в
# качестве делителя.

OP_EXIT = '0'
OP_PLUS = '+'
OP_MINUS = '-'
OP_MULTI = '*'
OP_DIVIDE = '/'
ERROR = 'error'

is_running = True


def math_operation(x1, x2, op):
    if op == OP_PLUS:
        return x1 + x2
    elif op == OP_MINUS:
        return x1 - x2
    elif op == OP_MULTI:
        return x1 * x2
    elif op == OP_DIVIDE and x2 != 0:
        return x1 / x2
    else:
        return ERROR


while is_running:
    x1 = float(input(f'Укажите число x1: '))
    x2 = float(input(f'Укажите число x2: '))
    op = input(f'Укажите операцию ({OP_PLUS}, {OP_MINUS}, {OP_MULTI}, {OP_DIVIDE} или {OP_EXIT} для выхода) : ')
    if op == OP_EXIT:
        is_running = False
        continue
    result = math_operation(x1, x2, op)
    if result == ERROR:
        print(f'Ошибка! попробуйте другие данные')
    else:
        print(f'Результат: {result}')

print(f'Программа завершена.')
