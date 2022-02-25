# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


code_char_min = 32
code_char_max = 127 + 1

result = ''
cnt = 1
for i in range(code_char_min, code_char_max):
    result += f'{bcolors.ENDC}{i:03d}:{bcolors.OKCYAN} {chr(i)}  '
    if cnt % 10 == 0:
        result += f'\n{bcolors.ENDC}'
    cnt += 1

print(result)

