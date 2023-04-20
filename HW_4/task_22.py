import random

n = int(input("Введите количество элементов первого набора чисел: "))
m = int(input("Введите количество элементов второго набора чисел: "))


fitst_list = [random.randint(-10, 10) for i in range(n)]
second_list = [random.randint(-10, 10) for i in range(n)]

first_set = set(fitst_list)
second_set = set(second_list)
total_set = first_set.union(second_set)

sorted_set = sorted(total_set)

print(sorted_set)