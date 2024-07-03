import functools
l = []
print("Введите строки из чисел. Чтобы закончить, введите нечисловую строку.")
while True:
    s = input()
    if not s.isnumeric():
        break
    l.append(s)
if len(l) < 1:
    print("Числовых строк введено не было.")
    exit()
b = False
for s in l:
    if s[0] != "0":
        b = True
        break
if not b:
    print("Корректного числа не получится, так как все числовые строки начинаются с нуля.")
    exit()


def compare_num_str(a, b):
    ab = a+b
    ba = b+a
    if ab < ba:
        return -1
    elif ab > ba:
        return 1
    return 0


l.sort(key = functools.cmp_to_key(compare_num_str), reverse = True)
print("".join(l))