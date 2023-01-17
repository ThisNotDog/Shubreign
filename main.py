#rogue-like rpg
import random
import os
import sys
from shop_and_items import *
from events import *
from dungeon import *
#player class holds attributes and amount of gold
class Player:
    def __init__(self, name, hp, attack, defense, day, current_hp, gold):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.day = day
        self.current_hp = current_hp
        self.gold = gold
    
    def __repr__(self):
        return f"your name is {self.name}\n your attack is: {self.attack}\n your defense is: {self.defense}\n"
class Items:
    def __init__(self, weapon, shield, consumable):
        self.weapon = weapon
        self.shield = shield
        self.consumable = consumable
        
#monster class holds enemy stats               
class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

#monster object for fight events
dargen_monster = Monster("dargen", 6, 1)

def get_fight_I(user, monster):
    print(f'you see a {monster.name}, are you prepared to fight?')
    
    i = input('press y to fight or n to run away\n')
    if i == "y":
        while user.current_hp > 0 and monster.hp > 0:
            player_hit = random.randint(0, user.attack)
            monster_hit = random.randint(0, monster.attack)
            print('you swing your weapon at the monster')
            monster.hp -= player_hit
            print(f'you have hit the monster for {player_hit} damage')
            if monster.hp <= 0:
                print('you have vanquished the monster and find coins in their pockets')
                user.gold += 20
                user.day += 1
            print('the monster attacks you')
            user.current_hp -= monster_hit
            print(f'you have been hit for {monster_hit} damage')
            if user.hp <= 0:
                print('you have died, game over')
                run = False
        user.day += 1
    else:
        user.day += 1
            

def main():
    user = Player("", 10, 1, 1, 1, 10, 0)
    user_items = Items("", "", "")
    name = input("welcome to the tyranic peninsula, what is your name?\n")
    if name != None:
        user.name = name
    if name == None:
        user.name = "idiot"
    print(f"hmm...{user.name}, pretty stupid name or whatever, let's just start\n")
    run = True
    while run == True and user.hp > 0:
        if user.day in (1, 4, 6):
            get_fight_I(user, dargen_monster)
            print(user.gold)
        if user.day in (2, 7, 8):
            get_random_event_I(user)
        if user.day == 3:
            dungeon_I(user)
        if user.day in (5, 9):
            get_shop_I(user)
        if user.day == 10:
            boss_I(user)
    run = False
if __name__ == '__main__':
    main()
