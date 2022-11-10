import random
import os
import sys
import datetime
import logging
import time
import items
import random_events
import pygame

#player class, holds the player attributes, current 'day' cycle, and amount of gold
class Player:
    def __init__(self, name, atk_lvl, defense_lvl, magic_lvl, hp_lvl, mp_lvl, day, gold):
        self.name = name
        self.atk_lvl = atk_lvl
        self.defense_lvl = defense_lvl
        self.magic_lvl = magic_lvl
        self.hp_lvl = hp_lvl
        self.mp_lvl = mp_lvl
        self.day = day
        self.gold = gold
    def get_total_level():
        total_lvl = 0
        total_lvl += self.atk_lvl
        total_lvl += self.defense_lvl
        total_lvl += self.magic_lvl
        total_lvl += self.hp_lvl
        total_lvl += self.mp_lvl
        print('your total level is {} great job or whatever'.format(str(total_lvl)))

    def __repr__(self):
        return '''your name is {}\nattack level: {}\n defense level: {}\n
        magic level: {}\n hp level: {}\n mp level: {}\n'''.format(self.name, self.atk_lvl, self.defense_lvl,
                                               self.magic_lvl, self.hp_lvl, self.mp_lvl)

class Status():
    def __init__(self, hp_lvl, mp_lvl):
        self.hp_lvl = hp_lvl
        self.mp_lvl = mp_lvl
    
class Equipment():
    def __init__(self, atk, defense):
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


rofl_420 = Monster('rofl 420', 5, 5, 10)
player = Player('player 1', 5, 5, 5, 20, 10, 1, 0)
player_equipment = Equipment(0, 0)
player_status = Status(player.hp_lvl, player.mp_lvl)


wait = time.sleep(1)
print(player)
def simple_fight(player, monster):
    player_hit = random.randrange(0, player.atk_lvl) - monster.defense_lvl
    while monster.hp_lvl > 0 and player.hp_lvl > 0:
        monster.hp_lvl -= player_hit
        print('you hit the monster for {}!\n'.format(player_hit))
        wait
        print('they now have {} hitpoints\n'.format(monster.hp_lvl))
        wait
        monster_hit = random.randrange(0, monster.atk_lvl) - player.defense_lvl
        player.hp_lvl -= monster_hit
        print('they hit you for {}\n'.format(monster_hit))
        wait
        print('your hp is now {}\n'.format(player.hp_lvl))
        wait
        if player.hp_lvl <= 0:
            print('you have perished')
        elif monster.hp_lvl <= 0:
            print('you have defeated the monster')
        else:
            raise ValueError("hp value's above 0")
    player.day += 1
    
#simple_fight(player, rofl_420)


#add_equipment('dog')
player.get_total_level
def wizard_dilemna(player):
    if player.day <= 5:
        input('in what dark the light shines brightest, known none of the past nor future?\n up or down will lead you toward the light, choose wisely\n')
        if input == 'up':
            print('wise choice, may i wish you good luck')
            k = random.randrange(1, 5)
            j = random.randrange(1, 4)
            if k == 1:
                player.atk_lvl +=  j
                print('your attack level has increased by {}\n'.format(str(j)))
            elif k == 2:
                player.defense_lvl += j
                print('your defense level has increased by {}\n'.format(str(j)))
            elif k == 3:
                player.magic_lvl += j
                print('your magic level has increased by {}\n'.format(str(j)))
            elif k == 4:
                player.hp_lvl += j
                print('your hp level has increased by {}\n'.format(str(j)))
            elif k == 5:
                player.mp_lvl += j
                print('your maximum mana has increased by {}'.format(str(j)))
        else:
            print('''
                  you have been given good fortune.\n
                  your attack, defense, and hp levels have increased\n
                  ''')
            player.atk_lvl += 1
            player.defense_lvl += 1
            player.hp_lvl +=2
            
    elif day >= 5:
        print('you notice a troll dancing in the moonlight\n')
        print('you feel stronger')
        player_status.hp_lvl = player.hp_lvl
        player_status.mp_lvl = player.mp_lvl
    else:
        raise ValueError('player.day is not btwn 0 to inf')
    player.day += 1
    
#stance event
def balancing_act(player):
    if player.day <= 5:
        input('''
            hello my good fellow, might i inquire you to hold
            this bucket on your head?\n
            ''')
        if input == 'yes':
            while player_status.hp_lvl > 0:
                count = 0
                weight_damage = random.randrange(0, int(player.hp_lvl / 7))
                print('''
                      well looky here, you can carry all that weight
                      without collapsing, but you appear to be taking
                      some damage
                      ''')
                player_status.hp_lvl -= weight_damage
                count += 1
        else:
            print('well just go off on your merry way then prick')
            
    else:
        print('your fortune has run dry my friend')
    player.day += 1

wizard_dilemna(player)
print(player)
