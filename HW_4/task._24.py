import random

n = int(input('Введите количество кустов: '))
ferility = [random.randint(1, 30) for i in range(n)]

count = []
for i in range(len(ferility) - 1):
    count.append(ferility[i - 1] + ferility[i] + ferility[i + 1])
count.append(ferility[-2] + ferility[-1] + ferility[0])
print(ferility)
print(count)
print(max(count))