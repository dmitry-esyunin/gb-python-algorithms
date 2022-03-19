# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
# являться минимальными), так и различаться.

def min_two_args(array):
    min1= array[0]
    min2= array[0]
    for i in array:
        if min1 > i:
            min1 = i
            min2 = min1

    return (min1, min2)


array = [1, 1, 2, 4, 8, 16, 32, 64, 128, 256]
(min1, min2) = min_two_args(array)

print(min1, min2)
