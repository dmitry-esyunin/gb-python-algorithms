# Определить, какое число в массиве встречается чаще всего.

array = [0, 0, 1, 1, 2, 2, 3, 3, 3]
freq = [0] * len(array)

for i in range(len(array)):
    freq[i] = len([x for x in array if x == array[i]])


print(f'                       массив  : {array}')
print(f'частота встречи его элементов  : {freq}')
print(f'число, которое встречается чаще всего: {array[freq.index(max(freq))]}')
