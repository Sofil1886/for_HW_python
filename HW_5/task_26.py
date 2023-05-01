a = int(input('Введите число а: '))
b = int(input('Введите число б: '))

def calculate(first, second):
    if second == 0:
        return 1
    else:
        return first * calculate(first, second - 1)

res = calculate(a, b)
print(res)