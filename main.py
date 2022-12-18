import random
import os
import re

#rogue-like rpg

#player class holds attributes and amount of gold
class Player:
    def __init__(self, name, hp, attack, defense, agility, day, gold):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.day = day
        self.gold = gold
    
    def __repr__(self):
        return '''your name is {}\n
                  your attack is: {}\n
                  your defense is: {}\n
                  your agility is: {}\n
                  your gold is: {}\n
                '''.format(name, hp, attack, defense, agility, gold)
 
#monster class holds enemy stats               
class Monster:
    def __init__(self, name, hp, hit_chance, dodge_chance):
        self.name = name
        self.hp = hp
        self.hit_chance = hit_chance
        self.dodge_chance = dodge_chance
  
user= Player("", 10, 1, 1, 1, 0, 20)
run = True
def main():
    input("welcome to the tyranic peninsula, what is your name?\n")
    user.name = input
    print("pretty stupid name or whatever, let's just start\n".format(user.name))
    while run == True and user.hp > 0:
        i = range(1,11)
        if i == 1 or i == 4 or i == 6:
            get_fight_I
        if i == 2 or i == 7 or i == 8:
            get_random_event_I
        if i == 3:
            get_dungeon_I
        if i == 5 or i == 9:
            get_shop_I
        if i == 10:
            boss_I
            
        
        
        
        
