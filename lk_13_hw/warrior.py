from random import randint, choice
from typing import NamedTuple


class Weapon(NamedTuple):
    name: str
    power: int


class Warrior:
    def __init__(self, weapon: Weapon, name: str, health: int):
        self.weapon = weapon
        self.name = name
        self.health = health
        self.armor = randint(1, 101)
        self.status = 'alive'

    def add_health(self, value):
        if value < 0:
            print('Слишком мало')
            return
        self.health += value

    def change_weapon(self, weapon):
        self.weapon = weapon

    def add_armor(self, armor):
        if armor < 0:
            print('Слишком мало')
            return
        self.armor += armor

    def hit_other(self, other_warrior):
        if other_warrior.status == 'die':
            print(other_warrior.name + 'is die')
            raise Exception
        if other_warrior.armor:
            predict = other_warrior.armor - self.weapon.power
            if predict < 0:
                other_warrior.armor -= self.weapon.power + predict
                other_warrior.health += predict
                return
            other_warrior.armor -= self.weapon.power
            return
        predict = other_warrior.health - self.weapon.power
        if predict < 0:
            other_warrior.status = 'die'
            return
        other_warrior.health -= self.weapon.power


def random_choose_weapon():
    weapon_list = []
    for i in range(50):
        weapon_list.append(Weapon(
            name=str(i),
            power=randint(1, 101)
        ))
    return choice(weapon_list)


def fight():
    warrior1 = Warrior(name='Naruto', health=100, weapon=random_choose_weapon())
    warrior2 = Warrior(name='Sasuke', health=100, weapon=random_choose_weapon())
    while True:
        print(warrior1.weapon.power, 'ninja')
        print(warrior2.weapon.power, 'traitor')
        print(warrior2.health)
        print(warrior2.armor)
        print(warrior1.health, 'ninja')
        print(warrior1.armor, 'ninja')
        warrior1.hit_other(warrior2)
        print(warrior2.health)
        print(warrior2.armor)
        warrior1.hit_other(warrior2)
        print(warrior2.health)
        print(warrior2.armor)
        warrior2.hit_other(warrior1)
        print(warrior1.health)
        print(warrior1.armor)


fight()
