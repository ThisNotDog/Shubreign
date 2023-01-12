#rogue-like rpg
import random
import os
import sys
from . shop_and_items import *
from . import events
from . import dungeons
#player class holds attributes and amount of gold
class Player:
    def __init__(self, name, hp, attack, defense, day, current_hp):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.day = day
        self.current_hp = current_hp
    
    def __repr__(self):
        return '''
               your name is {}\n
               your attack is: {}\n
               your defense is: {}\n
               your gold is: {}\n
               '''.format(name, hp, attack, defense, gold)
class Item:
    def __init__(self, weapon, shield, consumable, gold):
        self.weapon = weapon
        self.shield = shield
        self.consumable = consumable
        self.gold = gold
        
#monster class holds enemy stats               
class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

#monster object for fight events
dargen_monster = Monster("dargen", 6, 1)

def get_fight_I(monster):
    print('you see a {}, are you prepared to fight?'.format(monster.name))
    
    i = input('press y to fight or n to run away\n')
    if i == "y":
        while user.current_hp > 0 and monster.hp > 0:
            player_hit = random.randint(0, user.attack)
            monster_hit = random.randint(0, monster.attack)
            print('you swing your weapon at the monster')
            monster.hp -= player_hit
            print('you have hit the monster for {} damage'.format(player_hit))
            if monster.hp <= 0:
                print('you have vanquished the monster and find coins in their pockets')
                user.gold += 20
                user.day += 1
            print('the monster attacks you')
            user.current_hp -= monster_hit
            print('you have been hit for {} damage'.format(monster_hit))
            if user.hp <= 0:
                print('you have died, game over')
                run = False
    else:
        user.day += 1
            
user = Player("", 10, 1, 1, 1, 1, 20, 10)
user_items = Items("", "", "")
def main():
    name = input("welcome to the tyranic peninsula, what is your name?\n")
    if name != None:
        user.name == name
    if name == None:
        user.name == "idiot"
    print("hmm...{}, pretty stupid name or whatever, let's just start\n".format(user.name))
    run = True
    while run == True and user.hp > 0:
        if user.day in (1, 4, 6):
            get_fight_I(user, dargen)
            print(user.gold)
        if user.day in (2, 7, 8):
            get_random_event_I()
        if user.day == 3:
            dungeon.get_dungeon_I()
        if user.day in (5, 9):
            get_shop_I()
        if user.day == 10:
            boss_I()
    run = False
main()   
        
        
        
        
