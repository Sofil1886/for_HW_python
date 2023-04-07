# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).


n = int(input('Количество долек по вертикали '))
m = int(input('Количество долек по горизонтали '))
k = int(input('Количество искомых долек '))

count_yes = 0
if k > n * m:
    print('No')
elif k % n == 0 or k % m == 0:
    print('Yes')
else:
    for i in range(1, n):
        if k == i * m or k == m + (n - i):
            count_yes += 1
        else:
            for i in range(1, m):
                if k == i * n or k == n + (m - i):
                    count_yes += 1
                else:
                    continue
    if count_yes > 0:
        print('Yes')
    else:
        print('No')