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
            user.hp -= 1
    
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
            user.current_hp -= 3
def radio_obstacle(user):
    print("you hear a radio playing in the distance\n")
    choice = input("type y to investigate, n to leave")
    if choice != "y":
        pass
    if choice == "y":
        i = random.randint(1, 2)
        if i == 1:
            print("you feel a surge of power\n your attack has been raised by 3")
            user.attack += 3
        if i == 2:
            print("you feel a surge of power\n your defense has been raised by 3")
            user.defense += 3
    
def lonely_shoe_obstacle(user):
    print("you see a shoe on the ground\n")
    choice = input("type y to pick it up, n to leave")
    if choice != "y":
        pass
    if choice == "y":
        i = random.randint(1, 2)
        if i == 1:
            print("you feel a surge of power\n your attack has been raised by 1")
            user.attack += 1
        if i == 2:
            print("you feel a surge of power\n your defense has been raised by 1")
            user.defense += 1

def dungeon_I(user):
    """
    Handles the dungeon exploration for the user.
    
    Parameters:
    user (Player): The player object.
    """
    for _ in range(5):       
        r = random.randint(1, 5)
        if r == 1:
            cliff_obstacle(user)
        elif r == 2:
            ganome_obstacle(user)
        elif r == 3:
            patchy_obstacle(user)
        elif r == 4:
            radio_obstacle(user)
        elif r == 5:
            lonely_shoe_obstacle(user)
    user.day += 1

def dungeon_II(user):
    """
    Handles the dungeon exploration for the user.
    
    Parameters:
    user (Player): The player object.
    """
    for _ in range(5):       
        r = random.randint(1, 5)
        if r == 1:
            cliff_obstacle(user)
        elif r == 2:
            ganome_obstacle(user)
        elif r == 3:
            patchy_obstacle(user)
        elif r == 4:
            radio_obstacle(user)
        elif r == 5:
            lonely_shoe_obstacle(user)
    user.day += 1

def dungeon_III(user):
    """
    Handles the dungeon exploration for the user.
    
    Parameters:
    user (Player): The player object.
    """
    for _ in range(5):       
        r = random.randint(1, 5)
        if r == 1:
            cliff_obstacle(user)
        elif r == 2:
            ganome_obstacle(user)
        elif r == 3:
            patchy_obstacle(user)
        elif r == 4:
            radio_obstacle(user)
        elif r == 5:
            lonely_shoe_obstacle(user)
    user.day += 1

