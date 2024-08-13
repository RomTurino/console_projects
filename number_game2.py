import random
import math

def input_number(prompt:str):
    '''
    Input positive number in infinite loop
    '''
    num = " "
    while not num.isdigit():  
        num = input(prompt)
    return int(num)



print("Это игра \"загадай число\". В этой игре вы загадываете число, а я угадываю.")

min_num = input_number("Введите минимальное число: ")
max_num = input_number("Введите максимальное число: ")


tries = math.ceil(math.log2(max_num - min_num))
print(f'Загадайте от {min_num} до {max_num}. Мне нужно попыток: {tries} ')
input("Нажмите Enter для продолжения")
while tries > 0:
    comp_number = (min_num + max_num)//2
    your_answer = input(f"{comp_number} - это ваше число? (да, больше, меньше): ")
    if your_answer not in ["да", "меньше", "больше"]:
        print("Введите \"да\", если я угадал, \"больше\", если мое число больше вашего, либо \"меньше\", если меньше")
        continue
    if your_answer == "меньше":
        max_num = comp_number - 1
        print(f"Ваше число меньше, понял. Значит ищу от {min_num} до {max_num}")
    elif your_answer == "больше":
        min_num = comp_number + 1
        print(f"Ваше число больше, понял. Значит ищу от {min_num} до {max_num}")
    else:
        print(f"Я угадал")
        break
    tries -= 1
    print(f"Осталось попыток: {tries}")
