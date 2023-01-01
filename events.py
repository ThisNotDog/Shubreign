#file for event functions
import random
def get_random_event_I(user):
    i = 1   #random.randint(1, 3)
    if i == 1:
        mister_wizard_event_I(user)
    if i == 2:
        sneeple_snopple_event_I(user)
    if i == 3:
        scary_frog_event_I(user)
    
def get_random_event_II(user):
    i = random.randint(1, 3)
    if i == 1:
        mister_wizard_event_II(user)
    if i == 2:
        sneeple_snopple_event_II(user)
    if i == 3:
        scary_frog_event_II(user)

def get_random_event_III(user):
    i = random.randint(1, 3)
    if i == 1:
        mister_wizard_event_III(user)
    if i == 2:
        sneeple_snopple_event_III(user)
    if i == 3:
        scary_frog_event_III(user)

def scary_frog_event_I(user):
    print('''
          ribbt.....ribbt....
          ''')
    desire = input('''
                   the frog appears to speak in tongue, and reaches out a hand.\n
                   type y to grab their hand, n to pass by
                   ''')
    if desire == "y":
        print('''
              the frog latches onto your arm, but it doesn't hurt, it actually feels great\n
              ''')
        user.defense += 1
        user.hp += 2
        print("your defense has been raised by 1\n your hp has been raised by 2")
    else:
        print('''
              the frog eyes you with its indeterminable gaze\n
              as you pass you feel yourself become lighter
              ''')
        user.gold += 10
        print("you have gained 10 gold")
    
    
def sneeple_snopple_event_I(user):
    print('''
          argargar i am the sneeple snopple what say ye?\n
          i implore your tarnished self to free me from my misery
          ''')
    desire = input("press y to free the sneeple snopple or n to not")
    if desire == "y":
        print('''
              the vase be merciful for i am free\n
              take this as a reward
              ''')
        user.gold += 20
    else:
        print('''
              cautious are those who have something to lose\n
              i pity you, and so, restore your power, begone
              ''')
        
def mister_wizard_event_I(user):
    print('''
          well hello there, you look spiffy...unlike my ex-wife. \n
          now would you mind bending down and checking if my shoes are tied?\n
          ''')
    desire = input("press y for yes or n for no")
    if desire == "y":
        i = random.randint(1, 2)
        if i == 1:
            print('''
                  well done lad, a bachelor such as i should never tie shoes \n
                  now as a reward i shall cast a spell on you with my eyes closed \n
                  best of luck!
                  ''')
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
            print('''
                  just like my ex-wife, you're all the same \n
                  well i guess we'll play a little game \n
                  i'll close my eyes and cast an alchemy spell \n
                  if i win i take money from you and if you win, well i guess you get some
                  ''')
            x = random.randint(1, 2)
            if x == 1:
                print("dagnabbit, i guess you win, take your spoils and leave")
                user.gold += 20
            if x == 2:
                print("yippy! get rekt lmao")
                user.gold -= 5
        user.day += 1

# def mister_wizard_event_II(user):
#     print('''my wife...wife...it's over i'm finished i... \n
#              i just need clay...needclay...inawpsneed;adpoe clay\n
#           ''')
#     desire = input("press y to dig for clay, press no to pat him on the back")
#     if desire == "y":
#         i = random.randint(1, 2)
#         if i == 1:
#             print('''clay...give me the clay...clay is good\n
#                   ''')
#             x = random.randint(1, 3)
#             if x == 1:
#                 user.attack += 2
#                 print("your attack has increased by 2")
#             if x == 2:
#                 user.defense += 2
#                 print("your defense has increased by 2")
#             if x == 3:
#                 user.agility += 2
#                 print("your agility has increased by 2")
#     if desire == "n":
#         print('''roll the die, clay is the alpha and omega...\n
#                  uncover thee treachery and stand barren\n
#               ''')
#         x = random.randint(1, 6)
#         y = random.randint(1, 6)
#         if x > y:
#             print("you rolled: {}\n the wizard rolled: {}\n".format(y, x))
#             print('''the clay has spoken and carries dissent of your purpose\n
#                      gone are your pockets as clay's power grows\n
#                   ''')
#             user.gold -= 20
#         if x < y:
#             print('''clay...why have you forsaken me, what will pacify...\n
#                      i feel rotten...to be me, wrath runs rampant\n
#                   ''')
#             user.gold += 40
#         if x == y:
#             print('''oh merciful powerful clay...a beacon of change\n
#                      my tears are bountiful toward your predicament, change the world\n
#                   ''')
#             user.attack += 1
#             user.defense += 1
#             user.agility += 1
#             print("your attack, defense, and agility have increased by 1")
#         
#         user.day += 1
# 
#     
    
    