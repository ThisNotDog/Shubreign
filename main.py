#rogue-like rpg
import random
import os
import re
import time
import sys
from shop_and_items import *
from events import *
from dungeon import *

#player class holds attributes and amount of gold
class Player:
    def __init__(self, name, hp, attack, defense, agility, day, current_hp):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.day = day
        self.current_hp = current_hp
    
    def __repr__(self):
        return '''your name is {}\n
                  your attack is: {}\n
                  your defense is: {}\n
                  your agility is: {}\n
                  your gold is: {}\n
                '''.format(name, hp, attack, defense, agility, gold)
class Items():
    def __init__(self, weapon, shield, consumable, gold):
        self.weapon = weapon
        self.shield = shield
        self.consumable = consumable
        self.gold = gold
        
#monster class holds enemy stats               
class Monster:
    def __init__(self, name, hp, attack, hit_chance, dodge_chance):
        self.name = name
        self.hp = hp
        self.hit_chance = hit_chance
        self.dodge_chance = dodge_chance
        self.attack = attack

#monster object for fight events
dargen = Monster("dargen", 6, 1, .50, .30)

def get_fight_I(user, monster):
    print('you see a {}, are you prepared to fight?'.format(monster.name))
    
    i = input('press y to fight or n to run away\n')
    if i == "y":
        while user.hp > 0 and monster.hp > 0:
            player_hit = random.randint(user.attack, user.attack+2)
            monster_hit = random.randint(monster.attack, monster.attack+1)
            print('you swing your weapon at the monster')
            monster.hp -= player_hit
            time.sleep(1)
            print('the monster attacks you')
            user.hp -= monster_hit
        if monster.hp <= 0:
            print('you have vanquished the monster and find coins in their pockets')
            user.gold += 20
            user.day += 1
        if user.hp <= 0:
            print('you have died, game over')
            run = False
    else:
        user.day += 1
            
user = Player("", 10, 1, 1, 1, 1, 20, 10)
user_items = Items("", "", "")
get_shop_I(user)
def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
    start = input("welcome to the tyranic peninsula, what is your name?\n")
    user.name = start
    print("hmm...{}, pretty stupid name or whatever, let's just start\n".format(user.name))
    run = True
    while run == True and user.hp > 0:
        if user.day in (1, 4, 6):
            get_fight_I(user, dargen)
            print(user.gold)
        if user.day in (2, 7, 8):
            get_random_event_I(user)
        if user.day == 3:
            dungeon.get_dungeon_I
        if user.day in (5, 9):
            get_shop_I
        if user.day == 10:
            boss_I
    run = False
main()   
        
        
        
        