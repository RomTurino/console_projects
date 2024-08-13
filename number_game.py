import random
import math

min_num = "мин"
while not min_num.isdigit():  # повторять пока min_num - не число
    min_num = input("Введите минимальное число: ")
min_num = int(min_num)

max_num = "макс"
while not max_num.isdigit():  # повторять пока max_num - не число
    max_num = input("Введите максимальное число: ")
max_num = int(max_num)


tries = math.ceil(math.log2(max_num - min_num))
print(f'Компьютер загадал число от {min_num} до {max_num}. Твоя задача - угадать за {tries} попыток.')

secret_number = random.randint(min_num, max_num)
while tries > 0:
    my_number = input("Введите число: ")
    if not my_number.isdigit():
        print("Ай-яй-яй! Вы ввели не число.")
        continue

    my_number = int(my_number)
    if secret_number > my_number:
        print("Мое число больше")
    elif secret_number < my_number:
        print("Мое число меньше")
    else:
        print("Вы угадали!")
        break

    tries -= 1
    print(f"Осталось попыток: {tries}")
    if tries == 0:
        print(f"Попытки закончились. Увы, вы не отгадали. Было загадано число {secret_number}")
