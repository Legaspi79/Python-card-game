# Opponents cards

import random


class Op:
    def __init__(self, life_points):
        self.life_points = life_points


class Cards:
    def __init__(self, name, element, power, amount):
        self.name = name
        self.element = element
        self.power = power
        self.amount = amount


op = Op(5)

water1 = Cards("Garden Hose", "Water", 1, 3)
water2 = Cards("Waterfall", "Water", 2, 2)
water3 = Cards("Typhoon", "Water", 3, 1)
# water = Elements("Water Cards:", "Water")

fire1 = Cards("Bonfire", "Fire", 1, 3)
fire2 = Cards("Firework", "Fire", 2, 2)
fire3 = Cards("Forest Fire", "Fire", 3, 1)
# fire = Elements("Fire Cards:", "Fire")

wind1 = Cards("Cool Breeze", "Wind", 1, 3)
wind2 = Cards("Windmill", "Wind", 2, 2)
wind3 = Cards("Hurricane", "Wind", 3, 1)
# wind = Elements("Wind Cards:", "Wind")

earth1 = Cards("Rock Collection", "Earth", 1, 3)
earth2 = Cards("Canyon", "Earth", 2, 2)
earth3 = Cards("Fissure", "Earth", 3, 1)
# earth = Elements("Earth Cards:", "Earth")


water = [water1, water2, water3]
fire = [fire1, fire2, fire3]
wind = [wind1, wind2, wind3]
earth = [earth1, earth2, earth3]

# INVENTORY
elements = [water, fire, wind, earth]


def op_turn():
    element_choice = random.randint(0, 3)
    card_choice = random.randint(0, 2)
    # element_choice = 3
    # card_choice = 0

    # if elements[element_choice][card_choice].amount == 0:
    #     playable = False
    # else:
    #     playable = True

    op_card_name = elements[element_choice][card_choice].name
    op_card_amount = elements[element_choice][card_choice].amount
    op_card_element = elements[element_choice][card_choice].element
    op_card_power = elements[element_choice][card_choice].power
    op_card_played = elements[element_choice][card_choice]

    return op_card_played

# def op_check():
#     return op_turn()
