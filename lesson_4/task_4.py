name = input("Как се казваш?: ")
color = input("Кой е любимият ти цвят?: ")
food = input("Коя е любимата ти храна?: ")
animal = input("Кое е любимото ти животно?: ")
number = int(input("Кажи едно число от 1 до 10: "))

for num in range(1, number + 1):
    if num == 1:
        print(f"Ти сега имаш {num} опашка.")
    else:
        print(f"Ти сега имаш {num} опашки.")

tails_word = "опашки"
if number == 1:
    tails_word = "опашка"

print(f"Ти си {color} {food}{animal} с {number} {tails_word}. Супергерой с име {name}!💥")
