import random
n = int(input('Введите количество элементов в массиве: '))
x = int(input('Введите число: '))
list_values = [random.randint(0, 10) for i in range(n)]

list_diff = []
for i in list_values:
    diff = abs(x - i)
    list_diff.append(diff)

min = min(list_diff)
count = 0
for q in list_diff:
    if min == q:
        break
    else:
        count += 1
    
result = list_values[count]

print(list_values)
print(result)
