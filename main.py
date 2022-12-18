import random
import os
import re
import time
from events import get_random_event_I
#rogue-like rpg

#player class holds attributes, amount of gold, and current day
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
    def __init__(self, name, hp, attack, hit_chance, dodge_chance):
        self.name = name
        self.hp = hp
        self.hit_chance = hit_chance
        self.dodge_chance = dodge_chance
        self.attack = attack
#player object that holds stats, day, and gold
user= Player("", 10, 1, 1, 1, 1, 20)
#monster objects for fight events
dargen = Monster("dargen", 6, 1, .50, .30)

#fight scene mechanics, takes in monster and player objects
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
            
        
def main():
    start = input("welcome to the tyranic peninsula, what is your name?\n")
    user.name = start
    print("hmm...{}, pretty stupid name or whatever, let's just start\n".format(user.name))
    run = True
    while run == True and user.hp > 0:
        
        if user.day == 1 or user.day == 4 or user.day == 6:
            get_fight_I(user, dargen)
            print(user.gold)
        if user.day == 2 or user.day == 7 or user.day == 8:
            get_random_event_I(user)
        if user.day == 3:
            get_dungeon_I
        if user.day == 5 or user.day == 9:
            get_shop_I
        if user.day == 10:
            boss_I
    run = False
main()   
        
        
        
        
