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
