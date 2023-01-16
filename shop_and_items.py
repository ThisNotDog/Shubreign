# shop and items file
import random
def get_shop_I(user):
    a = "dagger"
    b = "plastic"
    c == "health potion"
    print("welcome to my shop\n i currently have three items\n a dagger for 15gp\n a plastic shield for 20gp\n and a health potion for 30gp\n which of these would you like?\n")
    count = 0
    while count < 4:
        pass
    
        

weapons_I = ("dagger", "sword", "hammer")
shields_I = ("plastic", "balsa", "iron")
consumables_I =("health potion", "attack potion", "defense potion")

weapon_dict = {
    "dagger": 1,
    "sword": 2,
    "hammer": 3
}
shield_dict = {
    "plastic": 1,
    "balsa": 2,
    "iron": 3
}
consumables_list = ["health potion", "rod of death"]


def add_weapon(item):
    user.weapon = item
    user.attack += weapon_dict[item]
    print(f'you have equipped {item}\n' + f'and your attack bonus is now: {user.attack}\n')
def remove_weapon(item):
    user.weapon = None
    user.attack -= weapon_dict[item]
    print(f'you have removed {item}\n')

def add_shield(user, item):
    user.shield = item
    user.defense += shield_dict[item]
    print(f'you have equipped {item}\n' + f'and your defense bonus is now: {user.attack}\n')

def remove_shield(item):
    user.shield = None
    user.defense -= shield_dict[item]
    print(f'you have removed {item}\n')
def use_health_potion(user):
    if user.hp > user.current_hp:
        user.current_hp = user.hp
    if user.hp == user.current_hp:
        print('you are already full hp')
    if user.hp <= user.current_hp:
        pass
    else:
        pass
            
