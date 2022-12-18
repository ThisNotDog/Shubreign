#file for event functions
def get_random_event_I(user):
    i = random.randint(1, 3)
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
    
def mister_wizard_event_I(user):
    print('''well hello there, you look spiffy...unlike my ex-wife. \n
             now would you mind bending down and checking if my shoes are tied?\n
          ''')
    input("press y for yes or n for no")
    if input == y:
        i = random.randint(1, 2)
        if i == 1:
            print('''well done lad, a bachelor such as i should never tie shoes \n
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
            print('''just like my ex-wife, you're all the same \n
                     well i guess we'll play a little game \n
                     i'll close my eyes and cast an alchemy spell \n
                     if i win i take money from you and if you win, well i guess you get some
                ''')
            x = random.randint(1, 2)
            if x == 1:
                print("dagnabbit, i guess you win, take your spoils and leave")
                user.gold += 20
            if x == 2:
                pprint("yippy! get rekt lmao")
                user.gold -= 5
        user.day += 1

def mister_wizard_event_II(user):
    print('''my wife...wife...it's over i'm finished i... \n
             i just need clay...needclay...inawpsneed;adpoe clay\n
          ''')
    input("press y to dig for clay, press no to pat him on the back")
    if input == y:
        i = random.randint(1, 2)
        if i == 1:
            print('''clay...give me the clay...clay is good\n
                  ''')
            x = random.randint(1, 3)
            if x == 1:
                user.attack += 2
                print("your attack has increased by 2")
            if x == 2:
                user.defense += 2
                print("your defense has increased by 2")
            if x == 3:
                user.agility += 2
                print("your agility has increased by 2")
    if input == n:
        print('''roll the die, clay is the alpha and omega...\n
                 uncover thee treachery and stand barren\n
              ''')
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        if x > y:
            print("you rolled: {}\n the wizard rolled: {}\n".format(y, x))
            print('''the clay has spoken and carries dissent of your purpose\n
                     gone are your pockets as clay's power grows\n
                  ''')
            user.gold -= 20
        if x < y:
            print('''clay...why have you forsaken me, what will pacify...\n
                     i feel rotten...to be me, wrath runs rampant\n
                  ''')
            user.gold += 40
        if x == y:
            print('''oh merciful powerful clay...a beacon of change\n
                     my tears are bountifulul to your predicament, change the world\n
                  ''')
            user.attack += 1
            user.defense += 1
            user.agility += 1
            print("your attack, defense, and agility have increased by 1")
        
        user.day += 1

    
    
    
    
    