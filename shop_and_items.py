# shop and items file
def get_shop_I(user):
    i = random.randint(1, 3)
    a = ""
    b = ""
    c = ""
    d = ""
    if i == 1:
        user.items += weapon_I.append("dagger")
    if i == 2:
        user.items += weapon_I.append("sword")
    if i == 3:
        user.items += weapon_I.append("hammer")
weapon_I = ("dagger", "sword", "hammer")
consumables_I =("health potion", "attack potion", "defense potion", "agility potion")

from collections import namedtuple
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
    print('you have equipped {}\n'.format(str(item)) + 'and your attack bonus is now: {}\n'.format(user.attack))
def remove_weapon(item):
    user.weapon = None
    user.attack -= weapon_dict[item]
    print('you have removed {}'.format(item))

def add_shield(item):
    user.shield = item
    user.defense += shield_dict[item]
    print('you have equipped {}\n'.format(item) + 'and your defense bonus is now: {}\n'.format(user.attack))

def remove_shield(item):
    user.shield = None
    user.defense -= shield_dict[item]
    print('you have removed\n'.format(item))
def use_health_potion(user):
    if user.hp > user.current_hp:
        user.current_hp = user.hp
    if user.hp == user.current_hp:
        print('you are already full hp')
    if user.hp <= user.current_hp:
        pass
    else:
        pass
            

