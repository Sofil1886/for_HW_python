# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

coins_amount = int(input('Write coins amount: '))

count_for_0 = 0
count_for_1 = 0
for i in range(coins_amount):
    coin_side = random.randint(0, 1)
    if coin_side == 1:
        count_for_1 +=1
    elif coin_side == 0:
        count_for_0 += 1

print(f'Min coin amount to be tossed - {min(count_for_0, count_for_1)}')
