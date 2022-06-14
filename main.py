import Cards
import EnemyCards
import random
import os
import sys



def play_again():
    redo = input("Play again? (Y/N): ").lower()
    if redo == "y":
        pass
    elif redo == "n":
        exit()


def check_power(user_power, computer_power):
    if user_power > computer_power:
        print("You have overpowered your opponent")
        EnemyCards.op.life_points -= 1
    elif user_power < computer_power:
        print("You were overpowered")
        Cards.player.life_points -= 1

    else:
        print("You and your opponent are equally matched")
    #Cards.player_turn().amount -= 1


def reaction_check(user_power, computer_power, effective):
    if effective:
        user_power += 1
    else:
        computer_power += 1
    check_power(user_power, computer_power)


def card_decrease(user_card, computer_card):
    user_card -= 1


def text(player_card, computer_card, player_power, computer_power, player_amount, computer_amount):
    print(f"You played {player_card} (Power: {player_power})")
    print(f"The opponent played {computer_card} (Power: {computer_power})")
    player_amount -= 1
    computer_amount -= 1


def play():

    user = Cards.player_turn()
    computer = EnemyCards.op_turn()
    if user.amount >= 1:
        text(user.name, computer.name, user.power, computer.power, user.amount, computer.amount)
        user.decrease_amount()
        match user.element:
            case "Water":
                if computer.element == "Earth":
                    reaction_check(user.power, computer.power, False )
                elif computer.element == "Fire":
                    reaction_check(user.power, computer.power, True)
                else:
                    check_power(user.power, computer.power)

            case "Fire":
                if computer.element == "Water":
                    reaction_check(user.power, computer.power, False)
                elif computer.element == "Wind":
                    reaction_check(user.power, computer.power, True)
                else:
                    check_power(user.power, computer.power)
            case "Wind":
                if computer.element == "Fire":
                    reaction_check(user.power, computer.power, False)
                elif computer.element == "Earth":
                    reaction_check(user.power, computer.power, True)
                else:
                    check_power(user.power, computer.power)
            case "Earth":
                if computer.element == "Wind":
                    reaction_check(user.power, computer.power, False)
                elif computer.element == "Water":
                    reaction_check(user.power, computer.power, True)
                else:
                    check_power(user.power, computer.power)
    elif user.amount == 0:
        print("you are out of those cards")


def game():
    n = True
    while n:
        play()
        if Cards.player.life_points == 0:
            print("You Have been defeated")
            n = False
        elif EnemyCards.op.life_points == 0:
            print("You have defeated the opposition! Gratata")
            n = False
        else:
            n += 1
    play_again()


game()
