input_text = input("Write your song sounds: ")
check_letters = 'аеёиоуыэюя'
lett_list = []
# input_text.split(" ")


for each in input_text.split():
    filtered = len(list(filter(lambda x: x in check_letters, each)))
    lett_list.append(filtered)

result = list(map(lambda x: x == lett_list[0], lett_list))

if all(result) == True:
    print("Парам пам-пам")
else:
    print("Пам парам")
