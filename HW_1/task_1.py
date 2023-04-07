    # Задача 2: Найдите сумму цифр трехзначного числа.

Number = str(input('Введите трехзначное число '))
if len(Number) != 3:
    print("Вы ввели не трехзначное число!")
else:
    sum = 0
    for dig in range(len(Number)):
        sum += int(Number[dig])
    print(sum)