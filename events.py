#file for event functions
import random
#gets random event
def get_random_event(user, event_type):
    """
    Gets a random event based on the event type.
    
    Parameters:
    user (Player): The player object.
    event_type (str): The type of event ('I', 'II', 'III').
    """
    event_mapping = {
        'I': [mister_wizard_event_I, sneeple_snopple_event_I, scary_frog_event_I],
        'II': [mister_wizard_event_II, sneeple_snopple_event_II, scary_frog_event_II],
        'III': [mister_wizard_event_III, sneeple_snopple_event_III, scary_frog_event_III]
    }
    
    if event_type not in event_mapping:
        raise ValueError("Invalid event type. Expected 'I', 'II', or 'III'.")
    
    event_list = event_mapping[event_type]
    event_index = random.randint(0, 2)
    
    try:
        event_list[event_index](user)
    except IndexError:
        raise ValueError("Event index out of range. This should not happen.")
    except TypeError:
        raise ValueError("Event function not defined. This should not happen.")
    except Exception as e:
        raise ValueError("An error occurred during the event: {}".format(e))
    

def scary_frog_event_I(user):
    """
    Handles the scary frog event for the user.
    
    Parameters:
    user (Player): The player object.
    """
    print("""
    ribbt.....ribbt....
    """)
    
    choice = input("""
    The frog appears to speak in tongue, and reaches out a hand.\n
    Type 'y' to grab their hand, 'n' to pass by: 
    """).strip().lower()
    
    if choice == "y":
        print("""
        The frog latches onto your arm, but it doesn't hurt, it actually feels great.
        """)
        user.defense += 1
        user.hp += 2
        print("Your defense has been raised by 1.\nYour HP has been raised by 2.")
    elif choice == "n":
        print("""
        The frog eyes you with its indeterminable gaze.
        As you pass, you feel yourself become lighter.
        """)
        user.gold += 10
        print("You have gained 10 gold.")
    else:
        print("Invalid choice. You stand still, unsure of what to do.")

def sneeple_snopple_event_I(user):
    """
    Handles the Sneeple Snopple event for the user.
    
    Parameters:
    user (Player): The player object.
    """
    print("""
    argargar i am the sneeple snopple what say ye?\n
    i implore your tarnished self to free me from my misery
    """)
    
    choice = input("Press 'y' to free the Sneeple Snopple or 'n' to not: ").strip().lower()
    
    if choice == "y":
        print("""
        The vase be merciful for I am free\n
        Take this as a reward
        """)
        user.gold += 20
        print("You have gained 20 gold.")
    elif choice == "n":
        print("""
        Cautious are those who have something to lose\n
        I pity you, and so, restore your power, begone
        """)
        user.hp = user.max_hp
        print("Your HP has been restored to maximum.")
    else:
        print("Invalid choice. You stand still, unsure of what to do.")

def mister_wizard_event_I(user):
    """
    Handles the Mister Wizard event for the user.
    
    Parameters:
    user (Player): The player object.
    """
    print("""
    Well hello there, you look spiffy...unlike my cat. 
    Now would you mind bending down and checking if my shoes are tied?
    """)
    
    choice = input("Press 'y' for yes or 'n' for no: ").strip().lower()
    
    if choice == "y":
        i = random.randint(1, 2)
        if i == 1:
            print("""
            Well done lad, a bachelor such as I should never tie shoes.
            Now as a reward I shall cast a spell on you with my eyes closed.
            Best of luck!
            """)
            x = random.randint(1, 3)
            if x == 1:
                user.attack += 1
                print("Your attack has been raised by 1.")
            elif x == 2:
                user.defense += 1
                print("Your defense has been raised by 1.")
            elif x == 3:
                user.agility += 1
                print("Your agility has been raised by 1.")
        elif i == 2:
            print("""
            Just like my ex-wife, you're all the same.
            Well I guess we'll play a little game.
            I'll close my eyes and cast an alchemy spell.
            If I win, I take money from you and if you win, well I guess you get some.
            """)
            x = random.randint(1, 2)
            if x == 1:
                print("Dagnabbit, I guess you win, take your spoils and leave.")
                user.gold += 20
            elif x == 2:
                print("Yippy! Get rekt lmao.")
                user.gold -= 5
    elif choice == "n":
        print("You chose not to help the wizard.")
    else:
        print("Invalid choice. You stand still, unsure of what to do.")
    
    user.day += 1

def scary_frog_event_II(user):
    """
    Handles the scary frog event for the user.
    
    Parameters:
    user (Player): The player object.
    """
    print("""
    ribbt.....ribbt....
    """)
    
    choice = input("""
    The frog appears to speak in tongue, and reaches out a hand.\n
    Type 'y' to grab their hand, 'n' to pass by: 
    """).strip().lower()
    
    if choice == "y":
        print("""
        The frog latches onto your arm, but it doesn't hurt, it actually feels great.
        """)
        user.defense += 1
        user.hp += 2
        print("Your defense has been raised by 1.\nYour HP has been raised by 2.")
    elif choice == "n":
        print("""
        The frog eyes you with its indeterminable gaze.
        As you pass, you feel yourself become lighter.
        """)
        user.gold += 10
        print("You have gained 10 gold.")
    else:
        print("Invalid choice. You stand still, unsure of what to do.")

def sneeple_snopple_event_II(user):
    """
    Handles the Sneeple Snopple event for the user.
    
    Parameters:
    user (Player): The player object.
    """
    print("""
    argargar i am the sneeple snopple what say ye?\n
    i implore your tarnished self to free me from my misery
    """)
    
    choice = input("Press 'y' to free the Sneeple Snopple or 'n' to not: ").strip().lower()
    
    if choice == "y":
        print("""
        The vase be merciful for I am free\n
        Take this as a reward
        """)
        user.gold += 20
        print("You have gained 20 gold.")
    elif choice == "n":
        print("""
        Cautious are those who have something to lose\n
        I pity you, and so, restore your power, begone
        """)
        user.hp = user.max_hp
        print("Your HP has been restored to maximum.")
    else:
        print("Invalid choice. You stand still, unsure of what to do.")

def mister_wizard_event_II(user):
    """
    Handles the Mister Wizard event for the user.
    
    Parameters:
    user (Player): The player object.
    """
    print("""
    Well hello there, you look spiffy...unlike my cat. 
    Now would you mind bending down and checking if my shoes are tied?
    """)
    
    choice = input("Press 'y' for yes or 'n' for no: ").strip().lower()
    
    if choice == "y":
        i = random.randint(1, 2)
        if i == 1:
            print("""
            Well done lad, a bachelor such as I should never tie shoes.
            Now as a reward I shall cast a spell on you with my eyes closed.
            Best of luck!
            """)
            x = random.randint(1, 3)
            if x == 1:
                user.attack += 1
                print("Your attack has been raised by 1.")
            elif x == 2:
                user.defense += 1
                print("Your defense has been raised by 1.")
            elif x == 3:
                user.agility += 1
                print("Your agility has been raised by 1.")
        elif i == 2:
            print("""
            Just like my ex-wife, you're all the same.
            Well I guess we'll play a little game.
            I'll close my eyes and cast an alchemy spell.
            If I win, I take money from you and if you win, well I guess you get some.
            """)
            x = random.randint(1, 2)
            if x == 1:
                print("Dagnabbit, I guess you win, take your spoils and leave.")
                user.gold += 20
            elif x == 2:
                print("Yippy! Get rekt lmao.")
                user.gold -= 5
    elif choice == "n":
        print("You chose not to help the wizard.")
    else:
        print("Invalid choice. You stand still, unsure of what to do.")
    
    user.day += 1

def scary_frog_event_III(user):
    """
    Handles the scary frog event for the user.
    
    Parameters:
    user (Player): The player object.
    """
    print("""
    ribbt.....ribbt....
    """)
    
    choice = input("""
    The frog appears to speak in tongue, and reaches out a hand.\n
    Type 'y' to grab their hand, 'n' to pass by: 
    """).strip().lower()
    
    if choice == "y":
        print("""
        The frog latches onto your arm, but it doesn't hurt, it actually feels great.
        """)
        user.defense += 1
        user.hp += 2
        print("Your defense has been raised by 1.\nYour HP has been raised by 2.")
    elif choice == "n":
        print("""
        The frog eyes you with its indeterminable gaze.
        As you pass, you feel yourself become lighter.
        """)
        user.gold += 10
        print("You have gained 10 gold.")
    else:
        print("Invalid choice. You stand still, unsure of what to do.")

def sneeple_snopple_event_III(user):
    """
    Handles the Sneeple Snopple event for the user.
    
    Parameters:
    user (Player): The player object.
    """
    print("""
    argargar i am the sneeple snopple what say ye?\n
    i implore your tarnished self to free me from my misery
    """)
    
    choice = input("Press 'y' to free the Sneeple Snopple or 'n' to not: ").strip().lower()
    
    if choice == "y":
        print("""
        The vase be merciful for I am free\n
        Take this as a reward
        """)
        user.gold += 20
        print("You have gained 20 gold.")
    elif choice == "n":
        print("""
        Cautious are those who have something to lose\n
        I pity you, and so, restore your power, begone
        """)
        user.hp = user.max_hp
        print("Your HP has been restored to maximum.")
    else:
        print("Invalid choice. You stand still, unsure of what to do.")

def mister_wizard_event_III(user):
    """
    Handles the Mister Wizard event for the user.
    
    Parameters:
    user (Player): The player object.
    """
    print("""
    Well hello there, you look spiffy...unlike my cat. 
    Now would you mind bending down and checking if my shoes are tied?
    """)
    
    choice = input("Press 'y' for yes or 'n' for no: ").strip().lower()
    
    if choice == "y":
        i = random.randint(1, 2)
        if i == 1:
            print("""
            Well done lad, a bachelor such as I should never tie shoes.
            Now as a reward I shall cast a spell on you with my eyes closed.
            Best of luck!
            """)
            x = random.randint(1, 3)
            if x == 1:
                user.attack += 1
                print("Your attack has been raised by 1.")
            elif x == 2:
                user.defense += 1
                print("Your defense has been raised by 1.")
            elif x == 3:
                user.agility += 1
                print("Your agility has been raised by 1.")
        elif i == 2:
            print("""
            Just like my ex-wife, you're all the same.
            Well I guess we'll play a little game.
            I'll close my eyes and cast an alchemy spell.
            If I win, I take money from you and if you win, well I guess you get some.
            """)
            x = random.randint(1, 2)
            if x == 1:
                print("Dagnabbit, I guess you win, take your spoils and leave.")
                user.gold += 20
            elif x == 2:
                print("Yippy! Get rekt lmao.")
                user.gold -= 5
    elif choice == "n":
        print("You chose not to help the wizard.")
    else:
        print("Invalid choice. You stand still, unsure of what to do.")
    
    user.day += 1

def get_random_event(user, event_type):
    """
    Gets a random event based on the event type.
    
    Parameters:
    user (Player): The player object.
    event_type (str): The type of event ('I', 'II', 'III').
    """
    event_mapping = {
        'I': [mister_wizard_event_I, sneeple_snopple_event_I, scary_frog_event_I],
        'II': [mister_wizard_event_II, sneeple_snopple_event_II, scary_frog_event_II],
        'III': [mister_wizard_event_III, sneeple_snopple_event_III, scary_frog_event_III]
    }
    
    if event_type not in event_mapping:
        raise ValueError("Invalid event type. Expected 'I', 'II', or 'III'.")
    
    event_list = event_mapping[event_type]
    event_index = random.randint(0, 2)
    
    try:
        event_list[event_index](user)
    except IndexError:
        raise ValueError("Event index out of range. This should not happen.")
    except TypeError:
        raise ValueError("Event function not defined. This should not happen.")
    except Exception as e:
        raise ValueError("An error occurred during the event: {}".format(e))

