# shop and items file
import random

weapons_I = ("dagger", "sword", "hammer")
shields_I = ("plastic", "balsa", "iron")
consumables_I = ("health potion", "attack potion", "defense potion")

weapon_dict = {
    "dagger": 15,
    "sword": 25,
    "hammer": 35
}
shield_dict = {
    "plastic": 20,
    "balsa": 30,
    "iron": 40
}
consumables_dict = {
    "health potion": 30,
    "attack potion": 40,
    "defense potion": 50
}

def get_shop_I(user):
    """
    Displays the shop items and handles the purchase process.
    
    Parameters:
    user (Player): The player object.
    """
    items = {
        "dagger": 15,
        "plastic shield": 20,
        "health potion": 30
    }
    
    print("Welcome to my shop\nI currently have three items:")
    for item, price in items.items():
        print(f"A {item} for {price}gp")
    
    choice = input("Which of these would you like to buy? (type 'exit' to leave): ").strip().lower()
    
    if choice in items:
        price = items[choice]
        if user.gold >= price:
            user.gold -= price
            if choice in weapon_dict:
                add_weapon(user, choice)
            elif choice in shield_dict:
                add_shield(user, choice)
            elif choice in consumables_dict:
                add_consumable(user, choice)
            print(f"You have bought a {choice}.")
        else:
            print("You don't have enough gold.")
    elif choice == 'exit':
        print("Thank you for visiting the shop.")
    else:
        print("Invalid choice. Please try again.")

def add_weapon(user, item):
    """
    Adds a weapon to the user's inventory and updates attack bonus.
    
    Parameters:
    user (Player): The player object.
    item (str): The weapon to add.
    """
    user.weapon = item
    user.attack += weapon_dict[item]
    print(f"You have equipped {item}.\nYour attack bonus is now: {user.attack}.")

def add_shield(user, item):
    """
    Adds a shield to the user's inventory and updates defense bonus.
    
    Parameters:
    user (Player): The player object.
    item (str): The shield to add.
    """
    user.shield = item
    user.defense += shield_dict[item]
    print(f"You have equipped {item}.\nYour defense bonus is now: {user.defense}.")

def add_consumable(user, item):
    """
    Adds a consumable to the user's inventory.
    
    Parameters:
    user (Player): The player object.
    item (str): The consumable to add.
    """
    user.consumables.append(item)
    print(f"You have added {item} to your inventory.")

def get_random_item():
    """
    Returns a random item from the shop.
    
    Returns:
    str: The random item.
    """
    items = list(weapon_dict.keys()) + list(shield_dict.keys()) + list(consumables_dict.keys())
    return random.choice(items)

def get_random_price(item):
    """
    Returns the price of an item.
    
    Parameters:
    item (str): The item to get the price of.
    
    Returns:
    int: The price of the item.
    """
    if item in weapon_dict:
        return weapon_dict[item]
    elif item in shield_dict:
        return shield_dict[item]
    elif item in consumables_dict:
        return consumables_dict[item]
    return 0

def get_random_weapon():
    """
    Returns a random weapon.
    
    Returns:
    str: The random weapon.
    """
    return random.choice(weapons_I)

def get_random_shield():
    """
    Returns a random shield.
    
    Returns:
    str: The random shield.
    """
    return random.choice(shields_I)

def get_random_consumable():
    """
    Returns a random consumable.
    
    Returns:
    str: The random consumable.
    """
    return random.choice(consumables_I)

def get_random_weapon_price(weapon):
    """
    Returns the price of a weapon.
    
    Parameters:
    weapon (str): The weapon to get the price of.
    
    Returns:
    int: The price of the weapon.
    """
    return weapon_dict[weapon]

def get_random_shield_price(shield):
    """
    Returns the price of a shield.
    
    Parameters:
    shield (str): The shield to get the price of.
    
    Returns:
    int: The price of the shield.
    """
    return shield_dict[shield]

def get_random_consumable_price(consumable):
    """
    Returns the price of a consumable.
    
    Parameters:
    consumable (str): The consumable to get the price of.
    
    Returns:
    int: The price of the consumable.
    """
    return consumables_dict[consumable]

def get_random_shop_item():
    """
    Returns a random shop item.
    
    Returns:
    str: The random shop item.
    """
    return random.choice(list(weapon_dict.keys()) + list(shield_dict.keys()) + list(consumables_dict.keys()))




