# -*- coding: utf-8 -*-

from termcolor import cprint
import random

CAT_FOOD = 'cat_food'
HUMAN_FOOD = 'human_food'
VERBOSE = False
native_print = cprint


class House:

    def __init__(self):
        self.money_in_home = 100
        self.dirt_in_home = 0
        self.food_in_fridge = {CAT_FOOD: 30, HUMAN_FOOD: 50}

    def __str__(self):
        return f'Денег в доме {self.money_in_home}, еды {self.food_in_fridge[HUMAN_FOOD]}, ' \
               f'еды для кота {self.food_in_fridge[CAT_FOOD]}, грязи {self.dirt_in_home} '

    def create_incidents(self, f_food=0, f_money=0):
        if f_food:
            self.food_in_fridge[HUMAN_FOOD] -= self.food_in_fridge[HUMAN_FOOD] / 2
        if f_money:
            self.money_in_home -= self.money_in_home / 2


class Mammal:
    def __init__(self, house, name, type_of_food, digestibility, serving_size):
        self.digestibility = digestibility
        self.house = house
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.type_of_food = type_of_food
        self.quantity_all_food = 0
        self.serving_size = serving_size

    def update(self):
        self.fullness = 30
        self.happiness = 100
        self.house.money_in_home = 100
        self.house.food_in_fridge = {CAT_FOOD: 30, HUMAN_FOOD: 50}

    def is_alive(self):
        return self.fullness > 0

    def eat(self):
        if self.house.food_in_fridge[self.type_of_food] >= 1:
            quantity_of_food = self.house.food_in_fridge[self.type_of_food]

            cur_food = quantity_of_food if quantity_of_food <= self.serving_size else self.serving_size

            cprint(f'{self.name} кушает', color='yellow')
            self.fullness += cur_food * self.digestibility
            self.house.food_in_fridge[self.type_of_food] -= cur_food
            self.quantity_all_food += cur_food
        else:
            self.fullness -= 5
            cprint(f'{self.name} нет еды', color='red')


class Human(Mammal):
    def __init__(self, name, house, serving_size):
        super().__init__(name=name, house=house, digestibility=1, serving_size=serving_size, type_of_food=HUMAN_FOOD)

    def is_alive(self):
        return self.happiness > 0 & super().is_alive()

    def __str__(self):
        return f'{self.name}, Счастье {self.happiness}, сытость {self.fullness}'

    def check_dirty(self):
        if self.house.dirt_in_home > 90:
            self.happiness -= 10
            cprint(f'{self.name} Слишком грязный дом!')

    def caress_cat(self):
        self.happiness += 5
        cprint(f'{self.name}, гладит кота', color='green')


class Husband(Human):
    def __init__(self, name, house, wage):
        super().__init__(name=name, house=house, serving_size=30)
        self.wage = wage

    def act(self):
        if self.is_alive():
            if self.fullness <= 20:
                self.eat()
            elif self.house.money_in_home <= 150:
                self.work()
            else:
                action = random.choice([self.work, self.gaming, self.gaming, self.caress_cat])
                action()
        else:
            cprint(f'{self.name}, умер', color='red')

    def work(self):
        cprint(f'{self.name} сходил на работу', color='blue')
        self.house.money_in_home += self.wage
        self.fullness -= 10

    def gaming(self):
        cprint(f'{self.name} Играл в танки', color='blue')
        self.fullness -= 10
        self.happiness += 20


class Wife(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house, serving_size=30)

        self.quantity_fur_coat = 0
        self.spend_money = 0

    def act(self):
        if self.is_alive():
            if self.house.food_in_fridge[HUMAN_FOOD] < 10:
                self.shopping()
            elif self.fullness <= 20:
                self.eat()
            elif self.house.dirt_in_home > 50:
                self.clean_house()
            elif self.house.food_in_fridge[CAT_FOOD] < 10:
                self.buy_eat_for_cat()
            elif self.house.money_in_home > 250:
                self.buy_fur_coat()
            else:
                action = random.choice([self.shopping, self.clean_house, self.buy_eat_for_cat, self.caress_cat])
                action()
        else:
            cprint(f'{self.name}, умер', color='red')

    def shopping(self):
        if self.house.money_in_home > 1:
            food_for_human = self.house.money_in_home if self.house.money_in_home < 80 else 80
            cprint(f'{self.name} сходила в магазин за едой', color='magenta')
            self.fullness -= 10
            self.house.money_in_home -= food_for_human
            self.house.food_in_fridge[HUMAN_FOOD] += food_for_human
            self.spend_money += food_for_human
        else:
            cprint(f'{self.name} деньги кончились!', color='red')

    def buy_fur_coat(self):
        cprint(f'{self.name} купила шубу', color='magenta')
        self.house.money_in_home -= 150
        self.fullness -= 10
        self.happiness += 60
        self.quantity_fur_coat += 1
        self.spend_money += 150

    def clean_house(self):
        cprint(f'{self.name} убралась дома', color='magenta')
        dirt = self.house.dirt_in_home if self.house.dirt_in_home < 100 else 100
        self.fullness -= 10
        self.house.dirt_in_home -= dirt

    def buy_eat_for_cat(self):
        if self.house.money_in_home > 1:
            food_for_cat = self.house.money_in_home if self.house.money_in_home < 60 else 60
            cprint(f'{self.name} купила еды коту', color='magenta')
            self.fullness -= 10
            self.house.money_in_home -= food_for_cat
            self.house.food_in_fridge[CAT_FOOD] += food_for_cat
            self.spend_money += food_for_cat
        else:
            cprint(f'{self.name} деньги кончились!', color='red')


class Cat(Mammal):
    def __init__(self, name, house):
        super().__init__(name=name, house=house, digestibility=2, serving_size=10, type_of_food=CAT_FOOD)

    def __str__(self):
        return f'{self.name}, сытость {self.fullness}'

    def act(self):
        if self.is_alive():
            if self.fullness <= 20:
                self.eat()
            else:
                action = random.choice([self.sleep, self.soil])
                action()
        else:
            cprint(f'{self.name}, умер', color='red')

    def sleep(self):
        self.fullness -= 10
        cprint(f'{self.name}, спит', color='yellow')

    def soil(self):
        self.fullness -= 10
        self.house.dirt_in_home += 5
        cprint(f'{self.name}, дерёт обои', color='red')


class Child(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house, serving_size=10)

    def act(self):
        if self.is_alive():
            if self.fullness <= 10:
                self.eat()
            else:
                self.sleep()
        else:
            cprint(f'{self.name}, умер', color='red')

    def sleep(self):
        self.fullness -= 5
        cprint('{}, спит'.format(self.name), color='cyan')

    def check_dirty(self):
        return cprint('{} Всегда счастлив!'.format(self.name), color='blue')


our_home = House()

quantity_of_cat = 3
wage = 200
all_alive = True

serge = Husband(name='Сережа', house=our_home, wage=wage)
masha = Wife(name='Маша', house=our_home)
kolya = Child(name='Коля', house=our_home)
residents = [serge, masha, kolya]

for cat in range(quantity_of_cat):
    catt = Cat(house=our_home, name='Кот №' + str(cat + 1))
    residents.append(catt)

for day in range(366):
    cprint('================== День {} =================='.format(day), color='red')

    for resident in residents:
        all_alive &= resident.is_alive()
        resident.act()

    masha.check_dirty()
    serge.check_dirty()
    kolya.check_dirty()
    our_home.dirt_in_home += 5

    if not all_alive:
        break

cprint(f'Денег потраченно: {masha.spend_money}, Шуб купленно: {masha.quantity_fur_coat}, денег в доме: {our_home.money_in_home}')
