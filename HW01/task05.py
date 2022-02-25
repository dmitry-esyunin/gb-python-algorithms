

sym1 = input('Укажите первую букву латинского алфавита: ').lower()
sym2 = input('Укажите вторую букву латинского алфавита: ').lower()

xa = ord('a')
x1 = ord(sym1)
x2 = ord(sym2)

pos1 = x1 - xa + 1
pos2 = x2 - xa + 1
dist = abs(pos2 - pos1)
q = dist - 1 if dist > 1 else 0

print(f'Позиция первой буквы в латинском алфавите: {pos1}')
print(f'Позиция второй буквы в латинском алфавите: {pos2}')
print(f'Количество букв между ними: {q}')
