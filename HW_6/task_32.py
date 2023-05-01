import random

m = int(input("Введите количество элементов массива: "))
max_number = int(input("Введите максимальное число: "))
min_number = int(input("Введите минимальное число: "))

a_list = [random.randint(-10, 10) for i in range(m)]

for i in a_list:
    if i >= min_number and i <= max_number:
        print(i)
    