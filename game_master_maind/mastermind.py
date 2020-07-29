# -*- coding: utf-8 -*-
from mastermind_engine import make_number, count_cows_and_bulls, you_win, check_number

make_number()
count_of_try = 0

while True:
    my_number = input('Введите число:')
    if not check_number(number=my_number):
        print('Введите 4-ёх значное число, без повторений, начиная не с 0 ')
        continue

    print(count_cows_and_bulls())
    count_of_try += 1

    if you_win():
        print('Вы победили!! Количество ходов:', count_of_try)

        if input('Хотите еще сыграть?') != 'да':
            break
        make_number()
        count_of_try = 0
