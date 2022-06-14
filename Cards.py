import random

import EnemyCards


class Player:
    def __init__(self, life_points):
        self.life_points = life_points


class Cards:
    def __init__(self, name, element, power, amount):
        self.name = name
        self.element = element
        self.power = power
        self.amount = amount

    def decrease_amount(self):
        self.amount -= 1

# class Turn(Cards):
#     def __init__(self, element_choice, card_choice):
#         self.element_choice = element_choice
#         self.card_choice = card_choice


# class Elements:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description

player = Player(5)

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


# water_dict = {"Water1": water1,
#               "Water2": water2,
#               "Water3": water3}


water = [water1, water2, water3]
fire = [fire1, fire2, fire3]
wind = [wind1, wind2, wind3]
earth = [earth1, earth2, earth3]

# INVENTORY
element_list = [water, fire, wind, earth]


def player_turn():
    print(f"HP: {player.life_points} / Opponent HP: {EnemyCards.op.life_points}")
    inc = 1
    for j in element_list:
        print(f"{inc}. {j[0].element}")
        inc += 1
    inc = 1
    element_choice = int(input("choose element "))

    for i in element_list[element_choice - 1]:
        print(f"{inc}. {i.name} - {element_list[element_choice - 1][inc-1].amount} left")
        inc += 1

    card_choice = int(input("Choose your card "))

    card_element = card_name = element_list[element_choice - 1][card_choice - 1].element
    card_name = element_list[element_choice - 1][card_choice - 1].name
    card_amount = element_list[element_choice - 1][card_choice - 1].amount
    card_object = element_list[element_choice - 1][card_choice - 1]
    card_power = element_list[element_choice - 1][card_choice - 1].power
    # print(card_amount)

    return card_object

    # for i in elements[choice - 1]:
    #     print(f"{inc}. {i.name}")
    #     inc += 1
    # play = int(input("Choose a card to play "))
    #
    # return {"Element": choice,
    #         "Card": play}

# "inventory" system
# all_cards = {"Water": water,
#              "Fire": fire}

# CALL ON ATTRIBUTE OF A CARD
# print(water[2]["Item"].power)
