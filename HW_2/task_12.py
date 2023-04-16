sum = int(input('Write sum: '))
prod = int(input('Write product: '))

D = sum**2 - 4 * prod
x1 = (sum + D**(1/2)) / 2
x2 = (sum - D**(1/2)) / 2

if x1 > 0 and x1 == int(x1):
    y1 = sum - x1
    print(f'First number is {x1}, second number is {y1}')
elif x2 > 0 and x2 == int(x2):
    y2 = sum - x2
    print(f'First number is {x2}, second number is {y2}')
else:
    print('Петя не загадал целые натуральные числа')