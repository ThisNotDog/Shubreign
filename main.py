import random
import os
import sys
import datetime
import logging
import time
import items
import random_events

#player class, holds the player attributes, and current 'day' cycle 
class Player:
    def __init__(self, name, atk_lvl, defense_lvl, magic_lvl, hp_lvl, mp_lvl, day, xp):
        self.name = name
        self.atk_lvl = atk_lvl
        self.defense_lvl = defense_lvl
        self.magic_lvl = magic_lvl
        self.hp_lvl = hp_lvl
        self.mp_lvl = mp_lvl
        self.day = day
        self.xp = xp
    def get_total_level():
        total_lvl = 0
        total_lvl += self.atk_lvl
        total_lvl += self.defense_lvl
        total_lvl += self.magic_lvl
        total_lvl += self.hp_lvl
        total_lvl += self.mp_lvl
        print('your total level is {} great job or whatever'.format(str(total_lvl)))

    def __repr__(self):
        return 'your name is {}\nattack level: {}\ndefense level: {}\nmagic level: {}\nhp level: {}\nmp level: {}\n'.format(self.name, self.atk_lvl, self.defense_lvl, self.magic_lvl, self.hp_lvl, self.mp_lvl)

class Status():
    def __init__(self, hp_lvl, mp_lvl):
        self.hp_lvl = hp_lvl
        self.mp_lvl = mp_lvl
    
class Equipment():
    def __init__(self, atk, defense, magic, hp, mp):
        self.atk = atk
        self.defense = defense
        
class Monster:
    def __init__(self, name, atk_lvl, defense_lvl, hp_lvl):
        self.name = name
        self.atk_lvl = atk_lvl
        self.defense_lvl = defense_lvl
        self.hp_lvl = hp_lvl

class Shop:
    def __innit__(self, item_dic):
        item_dic = self.item_dic
        
#item_shop_1 = Shop(items.items_1)
#item_shop_2 = Shop(items.items_2)
#item_shop_3 = Shop(items.items_3)

rofl_420 = Monster('rofl 420', 5, 5, 10)
player = Player('player 1', 5, 5, 5, 20, 10, 1, 0)
player_equipment = Equipment(0, 0, 0, 0, 0)
player_status = Status(player.hp_lvl, player.mp_lvl)


wait = time.sleep(1)
print(player)
def simple_fight(player, monster):
    while monster.hp_lvl > 0 and player_status.hp_lvl > 0:
            player_hit = random.randrange(0, player.atk_lvl) - monster.defense_lvl
            monster.hp_lvl -= player_hit
            print('you hit the monster for {}!\n'.format(player_hit))
            wait
            print('they now have {} hitpoints\n'.format(monster.hp_lvl))
            wait
            monster_hit = random.randrange(0, monster.atk_lvl) - player.defense_lvl
            player_status.hp_lvl -= monster_hit
            print('they hit you for {}\n'.format(monster_hit))
            wait
            print('your hp is now {}\n'.format(player_status.hp_lvl))
            wait
            if player.hp_lvl <= 0:
                print('you have perished')
            elif monster.hp_lvl <= 0:
                print('you have defeated the monster')
    player.day += 1
    
#simple_fight(player, rofl_420)


#add_equipment('dog')
player.get_total_level


random_events.wizard_dilemna(player.day)
player.get_total_level