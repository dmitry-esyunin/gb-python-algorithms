# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
# число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


class MyHex:
    def __init__(self, hex_):
        self.hex = list(hex_)

    def __add__(self, other):
        return list(str(hex(int(f'0x{str(self)}', 16) + int(f'0x{str(other)}', 16))).upper()[2:])

    def __mul__(self, other):
        return list(str(hex(int(f'0x{str(self)}', 16) * int(f'0x{str(other)}', 16))).upper()[2:])

    def __str__(self):
        return ''.join(self.hex)


def main():
    user_input = input('Укажите первое число (0 - для демо): ')
    if user_input == '0' or user_input == '':
        s1 = 'A2'
        s2 = 'C4F'
    else:
        s1 = user_input
        s2 = input('Укажите второе число: ')

    x1 = MyHex(s1)
    x2 = MyHex(s2)
    print(f'       сумма \'{x1}\' и \'{x2}\' равна: {x1 + x2}\nпроизведение \'{x1}\' и \'{x2}\' равно: {x1 * x2}\n')


if __name__ == "__main__":
    main()
