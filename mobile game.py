import os
import time
#import loot_table
#GLOBAL

races = [
    "Orclandia",
    "Pandalandia",
    "Lizardlandia"
    ]
specialities = [
    "Wizard...FIRE BALL",
    "Monk Dunkin on the Haters",
    "Paladin Philosophy",
    "Meth Chemistry"
    ]

#CHAR DETAILS#
class Player():
    def __init__(self, name, spec, race):
        self.name = name
        self.spec = spec
        self.race = race
    def __repr__(self):
        return "{} is a specialist in {} and resides from {}".format(self.name, self.spec, self.race)
    
#STATUS#
class Status(Player):
    def __init__(self, maxHP, maxMP, atk, armor, mr, spd):
        self.maxHP = maxHP
        self.maxMP = maxMP
        self.atk = atk
        self.armor = armor
        self.mr = mr
        self.spd = spd
        
    def get_player_status(maxHP, maxMP, atk, armor, mr, spd):
        return
        [(maxHP - Fight.damage),
        (maxMP - Fight.magic),
        (atk + Fight.strength),
        (armor + Fight.shield),
        (mr + Fight.lace),
        (spd + Fight.boots)]
        
#FIGHT INTERACTIONS#
class Gear():
    def __init__(self, damage, magic, strength, shield, lace, boots):
        self.damage = damage
        self.magic = magic
        self.strength = strength
        self.shield = shield
        self.lace = lace
        self.boots = boots
    def get_gear_status(damage, magic, strength, shield, lace, boots):
        pass
Carl = Player("Carl", specialities[3], races[0])
print(Carl)


