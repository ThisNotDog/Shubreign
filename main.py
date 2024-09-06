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
        self.day = 1
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
    print(f"you see a {monster.name}, are you prepared to fight?")

    i = input("press y to fight or n to run away\n")
    if i == "y":
        while user.current_hp > 0 and monster.hp > 0:
            player_hit = random.randint(0, user.attack)
            monster_hit = random.randint(0, monster.attack)
            print("you swing your weapon at the monster")
            monster.hp -= player_hit
            print(f"you have hit the monster for {player_hit} damage")
            if monster.hp <= 0:
                print("you have vanquished the monster and find coins in their pockets")
                user.gold += 20
                user.day += 1
            print("the monster attacks you")
            user.current_hp -= monster_hit
            print(f"you have been hit for {monster_hit} damage")
            if user.hp <= 0:
                print("you have died, game over")
                run = False
        user.day += 1
    else:
        user.day += 1

def get_random_event_I(user):
    #get random_event_I
    i = random.randint(1, 2)
    if i == 1:
        print("""
                you see a wizard in the distance, he beckons you to come closer\n
                he says "i have a gift for you, but you must choose wisely"\n
                """)
        x = random.randint(1, 3)
        if x == 1:
            user.attack += 1
            print("your attack has been raised by 1")
        if x == 2:
            user.defense += 1
            print("your defense has been raised by 2")
        if x == 3:
            user.agility += 1
            print("your agility has been raised by 3")
    if i == 2:
        print("""
              just like my ex-wife, you're all the same \n
              well i guess we'll play a little game \n
              i'll close my eyes and cast an alchemy spell \n
              if i win i take money from you and if you win, well i guess you get some
              """)
        x = random.randint(1, 2)
        if x == 1:
            print("dagnabbit, i guess you win, take your spoils and leave")
            user.gold += 20
        if x == 2:
            print("yippy! get rekt lmao")
            user.gold -= 5
    user.day += 1

def get_shop_I(user):
    print("""
            you see a shop in the distance, do you wish to enter?\n
            press y to enter or n to keep walking\n
            """)
    i = input()
    if i == "y":
        print("you enter the shop and see a merchant")
        print("the merchant says 'hello, what can i do for you today?'")
        print("press 1 to buy a sword for 10 gold")
        print("press 2 to buy a shield for 10 gold")
        print("press 3 to buy a potion for 5 gold")
        print("press 4 to leave the shop")
        i = input()
        if i == "1":
            if user.gold >= 10:
                print("you have bought a sword")
                user.attack += 2
                user.gold -= 10
            else:
                print("you don't have enough gold")
        if i == "2":
            if user.gold >= 10:
                print("you have bought a shield")
                user.defense += 2
                user.gold -= 10
            else:
                print("you don't have enough gold")
        if i == "3":
            if user.gold >= 5:
                print("you have bought a potion")
                user.current_hp += 5
                user.gold -= 5
            else:
                print("you don't have enough gold")
        if i == "4":
            print("you leave the shop")
        user.day += 1
    else:
        user.day += 1

def boss_I(user):
    """
    Handles the boss fight event for the user.
    
    Parameters:
    user (Player): The player object.
    """
    boss = Monster("boss", 10, 2)
    print("You see a large monster in the distance, are you prepared to fight?")
    
    choice = input("Press 'y' to fight or 'n' to run away: ").strip().lower()
    
    if choice == "y":
        while user.current_hp > 0 and boss.hp > 0:
            player_hit = random.randint(0, user.attack)
            boss_hit = random.randint(0, boss.attack)
            
            print("You swing your weapon at the boss.")
            boss.hp -= player_hit
            print(f"You have hit the boss for {player_hit} damage.")
            
            if boss.hp <= 0:
                print("You have vanquished the boss and find coins in their pockets.")
                user.gold += 50
                break  # Exit the loop since the boss is defeated
            
            print("The boss attacks you.")
            user.current_hp -= boss_hit
            print(f"You have been hit for {boss_hit} damage.")
            
            if user.current_hp <= 0:
                print("You have died, game over.")
                return False  # End the game if the user dies
        
        user.day += 1  # Increment the day after the fight
    else:
        print("You chose to run away from the boss.")
        user.day += 1  # Increment the day if the user runs away
    
    return True  # Continue the game if the user survives

def boss_II(user):
    boss = Monster("boss", 10, 2)
    print("you see a large monster in the distance, are you prepared to fight?")
    i = input("press y to fight or n to run away")
    if i == "y":
        while user.current_hp > 0 and boss.hp > 0:
            player_hit = random.randint(0, user.attack)
            boss_hit = random.randint(0, boss.attack)
            print("you swing your weapon at the boss")
            boss.hp -= player_hit
            print(f"you have hit the boss for {player_hit} damage")
            if boss.hp <= 0:
                print("you have vanquished the boss and find coins in their pockets")
                user.gold += 50
                user.day += 1
            print("the boss attacks you")
            user.current_hp -= boss_hit
            print(f"you have been hit for {boss_hit} damage")
            if user.hp <= 0:
                print("you have died, game over")
                run = False
        user.day += 1
    else:
        user.day += 1

def boss_III(user):
    boss = Monster("boss", 10, 2)
    print("you see a large monster in the distance, are you prepared to fight?")
    i = input("press y to fight or n to run away")
    if i == "y":
        while user.current_hp > 0 and boss.hp > 0:
            player_hit = random.randint(0, user.attack)
            boss_hit = random.randint(0, boss.attack)
            print("you swing your weapon at the boss")
            boss.hp -= player_hit
            print(f"you have hit the boss for {player_hit} damage")
            if boss.hp <= 0:
                print("you have vanquished the boss and find coins in their pockets")
                user.gold += 50
                user.day += 1
            print("the boss attacks you")
            user.current_hp -= boss_hit
            print(f"you have been hit for {boss_hit} damage")
            if user.hp <= 0:
                print("you have died, game over")
                run = False
        user.day += 1
    else:
        user.day += 1

beegen = Monster("beegen", 6, 1)

sleegen = Monster("sleegen", 6, 1)



def get_fight_II(user, monster):
    print(f"you see a {monster.name}, are you prepared to fight?")

    i = input("press y to fight or n to run away\n")
    if i == "y":
        while user.current_hp > 0 and monster.hp > 0:
            player_hit = random.randint(0, user.attack)
            monster_hit = random.randint(0, monster.attack)
            print("you swing your weapon at the monster")
            monster.hp -= player_hit
            print(f"you have hit the monster for {player_hit} damage")
            if monster.hp <= 0:
                print("you have vanquished the monster and find coins in their pockets")
                user.gold += 20
                user.day += 1
            print("the monster attacks you")
            user.current_hp -= monster_hit
            print(f"you have been hit for {monster_hit} damage")
            if user.hp <= 0:
                print("you have died, game over")
                run = False
        user.day += 1
    else:
        user.day += 1

def get_random_event_II(user):
    #get random_event_I
    i = random.randint(1, 2)
    if i == 1:
        print("""
                you see a wizard in the distance, he beckons you to come closer\n
                he says "i have a gift for you, but you must choose wisely"\n
                """)
        x = random.randint(1, 3)
        if x == 1:
            user.attack += 1
            print("your attack has been raised by 1")
        if x == 2:
            user.defense += 1
            print("your defense has been raised by 2")
        if x == 3:
            user.agility += 1
            print("your agility has been raised by 3")
    if i == 2:
        print("""
              just like my ex-wife, you're all the same \n
              well i guess we'll play a little game \n
              i'll close my eyes and cast an alchemy spell \n
              if i win i take money from you and if you win, well i guess you get some
              """)
        x = random.randint(1, 2)
        if x == 1:
            print("dagnabbit, i guess you win, take your spoils and leave")
            user.gold += 20
        if x == 2:
            print("yippy! get rekt lmao")
            user.gold -= 5
    user.day += 1

def get_shop_II(user):
    print("""
            you see a shop in the distance, do you wish to enter?\n
            press y to enter or n to keep walking\n
            """)
    i = input()
    if i == "y":
        print("you enter the shop and see a merchant")
        print("the merchant says 'hello, what can i do for you today?'")
        print("press 1 to buy a sword for 10 gold")
        print("press 2 to buy a shield for 10 gold")
        print("press 3 to buy a potion for 5 gold")
        print("press 4 to leave the shop")
        i = input()
        if i == "1":
            if user.gold >= 10:
                print("you have bought a sword")
                user.attack += 2
                user.gold -= 10
            else:
                print("you don't have enough gold")
        if i == "2":
            if user.gold >= 10:
                print("you have bought a shield")
                user.defense += 2
                user.gold -= 10
            else:
                print("you don't have enough gold")
        if i == "3":
            if user.gold >= 5:
                print("you have bought a potion")
                user.current_hp += 5
                user.gold -= 5
            else:
                print("you don't have enough gold")
        if i == "4":
            print("you leave the shop")
        user.day += 1
    else:
        user.day += 1

def boss_II(user):
    boss = Monster("boss", 10, 2)
    print("you see a large monster in the distance, are you prepared to fight?")
    i = input("press y to fight or n to run away")
    if i == "y":
        while user.current_hp > 0 and boss.hp > 0:
            player_hit = random.randint(0, user.attack)
            boss_hit = random.randint(0, boss.attack)
            print("you swing your weapon at the boss")
            boss.hp -= player_hit
            print(f"you have hit the boss for {player_hit} damage")
            if boss.hp <= 0:
                print("you have vanquished the boss and find coins in their pockets")
                user.gold += 50
                user.day += 1
            print("the boss attacks you")
            user.current_hp -= boss_hit
            print(f"you have been hit for {boss_hit} damage")
            if user.hp <= 0:
                print("you have died, game over")
                run = False
        user.day += 1
    else:
        user.day += 1

def get_fight_III(user, monster):
    print(f"you see a {monster.name}, are you prepared to fight?")

    i = input("press y to fight or n to run away\n")
    if i == "y":
        while user.current_hp > 0 and monster.hp > 0:
            player_hit = random.randint(0, user.attack)
            monster_hit = random.randint(0, monster.attack)
            print("you swing your weapon at the monster")
            monster.hp -= player_hit
            print(f"you have hit the monster for {player_hit} damage")
            if monster.hp <= 0:
                print("you have vanquished the monster and find coins in their pockets")
                user.gold += 20
                user.day += 1
            print("the monster attacks you")
            user.current_hp -= monster_hit
            print(f"you have been hit for {monster_hit} damage")
            if user.hp <= 0:
                print("you have died, game over")
                run = False
        user.day += 1
    else:
        user.day += 1

def get_random_event_III(user):
    #get random_event_I
    i = random.randint(1, 2)
    if i == 1:
        print("""
                you see a wizard in the distance, he beckons you to come closer\n
                he says "i have a gift for you, but you must choose wisely"\n
                """)
        x = random.randint(1, 3)
        if x == 1:
            user.attack += 1
            print("your attack has been raised by 1")
        if x == 2:
            user.defense += 1
            print("your defense has been raised by 2")
        if x == 3:
            user.agility += 1
            print("your agility has been raised by 3")
    if i == 2:
        print("""
              just like my ex-wife, you're all the same \n
              well i guess we'll play a little game \n
              i'll close my eyes and cast an alchemy spell \n
              if i win i take money from you and if you win, well i guess you get some
              """)
        x = random.randint(1, 2)
        if x == 1:
            print("dagnabbit, i guess you win, take your spoils and leave")
            user.gold += 20
        if x == 2:
            print("yippy! get rekt lmao")
            user.gold -= 5
    user.day += 1

def get_shop_III(user):
    print("""
            you see a shop in the distance, do you wish to enter?\n
            press y to enter or n to keep walking\n
            """)
    i = input()
    if i == "y":
        print("you enter the shop and see a merchant")
        print("the merchant says 'hello, what can i do for you today?'")
        print("press 1 to buy a sword for 10 gold")
        print("press 2 to buy a shield for 10 gold")
        print("press 3 to buy a potion for 5 gold")
        print("press 4 to leave the shop")
        i = input()
        if i == "1":
            if user.gold >= 10:
                print("you have bought a sword")
                user.attack += 2
                user.gold -= 10
            else:
                print("you don't have enough gold")
        if i == "2":
            if user.gold >= 10:
                print("you have bought a shield")
                user.defense += 2
                user.gold -= 10
            else:
                print("you don't have enough gold")
        if i == "3":
            if user.gold >= 5:
                print("you have bought a potion")
                user.current_hp += 5
                user.gold -= 5
            else:
                print("you don't have enough gold")
        if i == "4":
            print("you leave the shop")
        user.day += 1
    else:
        user.day += 1

def boss_III(user):
    boss = Monster("boss", 10, 2)
    print("you see a large monster in the distance, are you prepared to fight?")
    i = input("press y to fight or n to run away")
    if i == "y":
        while user.current_hp > 0 and boss.hp > 0:
            player_hit = random.randint(0, user.attack)
            boss_hit = random.randint(0, boss.attack)
            print("you swing your weapon at the boss")
            boss.hp -= player_hit
            print(f"you have hit the boss for {player_hit} damage")
            if boss.hp <= 0:
                print("you have vanquished the boss and find coins in their pockets")
                user.gold += 50
                user.day += 1
            print("the boss attacks you")
            user.current_hp -= boss_hit
            print(f"you have been hit for {boss_hit} damage")
            if user.hp <= 0:
                print("you have died, game over")
                run = False
        user.day += 1
    else:
        user.day += 1

user = Player("", 10, 1, 1, 1, 10, 0)
user_items = Items("", "", "")

def main():
    name = input("welcome to the tyranic peninsula, what is your name?\n")
    user.name = name if name else "idiot"
    print(f"hmm...{user.name}, pretty stupid name or whatever, let's just start\n")
    while user.hp > 0:
        if user.day == 1:
            get_fight_I(user, dargen_monster)
            print(user.gold)
        elif user.day in (2, 7, 8):
            get_random_event_I(user)
        elif user.day == 3:
            dungeon_I(user)
        elif user.day in (5, 9):
            get_shop_I(user)
        elif user.day == 10:
            boss_I(user)
        elif user.day in (11, 14, 16):
            get_fight_II(user, dargen_monster)
            print(user.gold)
        elif user.day in (12, 17, 18):
            get_random_event_II(user)
        elif user.day == 13:
            dungeon_II(user)
        elif user.day in (15, 19):
            get_shop_II(user)
        elif user.day == 20:
            boss_II(user)
        elif user.day in (21, 24, 26):
            get_fight_III(user, dargen_monster)
            print(user.gold)
        elif user.day in (22, 27, 28):
            get_random_event_III(user)
        elif user.day == 23:
            dungeon_III(user)
        elif user.day in (25, 29):
            get_shop_III(user)
        elif user.day == 30:
            boss_III(user)
        elif user.day == 31:
            print("you have completed the game, congratulations!")
            run = False
            sys.exit()
        else:
            print("you have died, game over")
            user.hp = 0
    run = False
    sys.exit()

if __name__ == "__main__":
    main()
