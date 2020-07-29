import random
from collections import Counter

computer_number = []
result = {}
my_number = []


def check_number(number='1'):
    global my_number
    my_number = number

    if not number.isdigit():
        return False
    if not 5 > len(number) > 3 or number[0] == '0':
        return False

    # проверка на уникальность
    check = Counter(number)
    for val in check.values():
        if val > 1:
            return False
    my_number = list(map(int, my_number))
    return True


def make_number():
    global computer_number

    first_number = random.randint(1, 9)
    computer_number = list(range(0, 10))
    computer_number.remove(first_number)
    computer_number = random.sample(computer_number, 3)
    computer_number.insert(0, first_number)


def count_cows_and_bulls():
    global result
    cow = 0
    bull = 0

    for my_number_check, computer_number_check in zip(my_number, computer_number):
        if my_number_check == computer_number_check:
            bull += 1
        elif my_number_check in computer_number:
            cow += 1

    result = {'коров': cow, 'быков': bull}
    return result


def you_win():
    return result['быков'] == 4
