input_text = input("Write your song sounds: ")
check_letters = list('аеёиоуыэюя')
lett_list = []
# input_text.split(" ")


for each in input_text.split():
    filtered = filter(lambda x: x in check_letters, each)
    let_amount = len(list(map(lambda x: x, filtered)))
    lett_list.append(let_amount)

result = list(map(lambda x: x == lett_list[0], lett_list))

if all(result) == True:
    print("Парам пам-пам")
else:
    print("Пам парам")
