# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
import random

num_min = 0
num_max = 100
num_max_try = 10
secret = random.randint(num_min, num_max)

is_win = False
try_left = num_max_try
while try_left > 0:
    print(f'У Вас осталось попыток: {try_left}')
    user_input = int(input(f"Введите число: "))
    if user_input == secret:
        is_win = True
        break
    elif user_input > secret:
        print(" << Перелет!")
    else:
        print("Недолет! >> ")
    try_left -= 1

if is_win:
    print("Попал!!! Поздравляю!")
else:
    print("Очень жаль, попробуйте еще раз")

