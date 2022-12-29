import random

def cliff_obstacle(user):
    print("what say yee? jump the cliff or turn back")
    choice = input("enter y or no")
    if choice != "y":
        pass
    if choice == "y":
        chance = random.randint(1, 2)
        if chance == 1:
            print("you take 2 damage and lose 10 gold")
            user.gold += 10
        if chance == 2:
            pass
        
def ganome_obstacle(user):
    print("hello there yungin, lift this rock off me\n")
    choice = input("type y to help, n to leave")
    if choice != "y":
        pass
    if choice == "y":
        i = random.randint(1, 2)
        if i == 1:
            print("you feel power surge inside you\n your attack has been raised by 2")
            user.attack += 2
        if i == 2:
            print("your feet feel a bit heavier\n")
            user.agility -= 1
    
def patchy_obstacle(user):
    print("you see a bush, do you search it?\n")
    choice = input("type y to search, n to leave")
    if choice != "y":
        pass
    if choice == "y":
        i = random.randint(1, 2)
        if i == 1:
            print("you feel your body grow stronger\n your defense has been raised by 2")
            user.defense += 2
        if i == 2:
            print("you feel your heart grow fainter\n your hp level has decreased by 3")
             -= 1
def radio_obstacle(user):
    print("4")
def lonelyShoe_obstacle(user):
    print("5")
def dungeon_I(user):
    count = 0
    for count in range(1, 6):        
        i = random.randint(1, 5)
        if i == 1:
            cliff_obstacle(user)
        if i == 2:
            ganome_obstacle(user)
        if i == 3:
            patchy_obstacle(user)
        if i == 4:
            radio_obstacle(user)
        if i == 5:
            lonelyShoe_obstacle(user)


