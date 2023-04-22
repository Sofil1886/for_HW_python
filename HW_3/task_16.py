import random
n = int(input('Введите количество элементов в массиве: '))
x = int(input('Введите число: '))

list_values = [random.randint(0, 10) for i in range(n)]
count = 0
for i in list_values:
    if x == i:
        count += 1

print(list_values)
print(count)