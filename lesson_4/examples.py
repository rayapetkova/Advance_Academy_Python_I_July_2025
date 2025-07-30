for number in range(1, 11):  # range = диапазон; range(1, 11) = всички числа от 1 до 10 включително
    print(number)

print("Цикълът приключи")


number = 7
user_num = int(input("Познай числото: "))

while user_num != number:
    user_num = int(input("Не позна! Опитай отново!: "))

print("Ти позна! Браво!")