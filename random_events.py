#random event file
import random
import main
#determines the pool of items available in shop, separated into 3 varying tiers,
#and raises an error to indicate whether they should/not be able to
def shop_event(day):
    if day < 5:
        item_shop_1
    elif day > 5 and day < 10:
        item_shop_2
    elif day > 10 and day < 15:
        item_shop_3
    else:
        raise ValueError("character has reached max time to shop or is bugged if Player.day <= 15")
        print("you have lost your ability to shop")
#decides which stance pool to choose between: 1-5 days and 6+ have different outcomes
def stance_event(day):
    if day <= 5:
        get_stance_event
    elif day >= 6:
        get_stance_event_2
        
#decides which skill pool to choose between: 1-5 days and 6+ have different outcomes
def skill_event(day):
    if day <= 5:
        get_stance_event
    elif day >= 6:
        get_stance_event_2
#decides which random event pool to choose between: 1-5 days and 6+ have different outcomes
def get_rand_event(day):
    if day <= 5:
        event = random.randrange(1, 2)
        if event == 1:
            random_events.get_stance_event
        elif event == 2:
            random_events.get_skill_event
    elif day >= 6:
        event = random.randrange(1, 2)
        if event == 1:
            random_events.get_stance_event_2
        elif event == 2:
            random_events.get_skill_event_2
#stance event: 
def wizard_dilemna(day):
    if day <= 5:
        input('in what dark the light shines brightest, known none of the past nor future?\n type up or down\n')
        
        if input() == 'up':
            print('wise choice, may i wish you good luck\n')
            k = random.randrange(1, 5)
            j = random.randrange(1, 4)
            if k == 1:
                player.atk_lvl +=  j
                print('your attack level has increased by {}\n'.format(str(j)))
            elif k == 2:
                player.defense_lvl += j
                print('your defense level has increased by {}\n'.format(str(j)))
            elif k == 3:
                player.magic_lvl += j
                print('your magic level has increased by {}\n'.format(str(j)))
            elif k == 4:
                player.hp_lvl += j
                print('your hp level has increased by {}\n'.format(str(j)))
            elif k == 5:
                player.mp_lvl += j
                print('your maximum mana has increased by {}\n'.format(str(j)))
        else:
            player.atk_lvl += 1
            player.defense_lvl += 1
            player.hp_lvl +=2
#stance event
def good_troll(day):
    if day <= 5:
        pass
    else:
        pass
        
                