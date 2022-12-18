from collections import namedtuple

def add_atk_equipment(item):
    player_1_equipment.atk += items.atk_items_1[item]
    player_1.atk_lvl += items.atk_items_1[item]
    print('you have equipped {}\n'.format(str(item)) + 'and your attack bonus is now: {}\n'.format(player_1_equipment.atk))

def add_def_equipment(item):
    player_1_equipment.defense += items.def_items_1[item]
    player_1.defense_lvl += items.def_items_1[item]
    print('you have equipped {}\n'.format(str(item)) + 'and your defense bonus is now: {}\n'.format(player_1_equipment.defense))

def use_health_potion(item):
    if player_1.Current.hp_lvl < player_1.hp_lvl:
        if player_1.Current.hp_lvl + 20 > player_1.hp_lvl:
            player_1.Current.hp_lvl = player_1.hp_lvl
        else:
            player_1.Current.hp_lvl += 20
    else:
        raise ValueError('players current hp is either full or bugged')
            
        
#offensive items dictionary
atk_items_1 = {
    'dog': 1
}
atk_items_2 = {
    'sonic hat': 2
}
atk_items_3 = {
    'auger': 3
}

#defensive items dictionary
def_items_1 = {
    'sleeveless shirt': 1
}
def_items_2 = {
    'tin foil hat': 2
}
def_items_3 = {
    'faraday cage': 3
}

#consumable dictionary
