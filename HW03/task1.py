#
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
#

NUM_START = 2
NUM_FINISH = 99
Rat = range(2, 9 + 1)
Res = [0] * len(Rat)

for number in range(NUM_START, NUM_FINISH + 1):
    for i, val in enumerate(Rat):
        if number % val == 0:
            Res[i] += 1

for i, val in enumerate(Rat):
    print(f'в диапазоне чисел от {NUM_START} до {NUM_FINISH} количество кратных числу {val}: {Res[i]}')








