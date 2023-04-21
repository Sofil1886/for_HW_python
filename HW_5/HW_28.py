a = int(input('Введите целое неотрицательное число а: '))
b = int(input('Введите целое неотрицательное число б: '))


def calculate_sum(a, b):
    if b == 0:
        return 1
    else:
        return a + calculate_sum(a/a, b - 1)

if a < 0 or b < 0:
    print('Введите неотрицательное число')
else:
    print(calculate_sum(a, b))