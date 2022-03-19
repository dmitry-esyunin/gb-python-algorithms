# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

array = random.sample(range(100), 10)
print(array)

min_index = 0
min_val = array[min_index]
max_index = 0
max_val = array[max_index]

for i, val in enumerate(array):
    if val < min_val:
        min_val = val
        min_index = i

    if val > max_val:
        max_val = val
        max_index = i

array[min_index] = max_val
array[max_index] = min_val

print(f'array[{min_index}] = {max_val}\narray[{max_index}] = {min_val}')
print(array)



