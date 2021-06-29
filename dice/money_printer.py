import math

import random
import time

def go():
    money = 50

    original_bet = 0.02
    bet = original_bet

    max = 0
    mini = 150

    loss_count = 0
    chosen_colour = 1

    multiplier = 1.65

    lower_bound = 0
    upper_bound = 100

    

    loss_list = [0 for x in range(20)]

    def play(bet, colour):
        spin = random.randint(0, 100)
        if spin >= 55:
            return bet * 2.2
        else:
            return 0


    while money > lower_bound and money < upper_bound :
        
        if won_last:
            bet = original_bet
            winnings = play(bet, chosen_colour)
            if winnings > 0:
                won_last = True
                loss_list[loss_count] += 1
                loss_count=0
            else:
                loss_count += 1
                won_last = False
            money = money - bet + winnings

        else:

            bet = bet * multiplier
            winnings = play(bet, chosen_colour)
            if winnings > 0:
                won_last = True
                loss_list[loss_count] += 1
                loss_count=0
                
            else:
                loss_count += 1
                won_last = False
            money = money - bet + winnings


        if money > max:
            max = money
        if money < mini:
            mini = money
    return money
    # time.sleep(0.05)

    # if chosen_colour == 1:
    #     chosen_colour = 0
    # else:
    #     chosen_colour = 1
    # print("Win?: ",won_last, end="    ")
    # print("Cash: ",money, end="    ")
    # print("Bet: ",bet)
# print(money)
# print(max)
# print(mini)
# print(loss_list)

w = 0
l = 0
for i in range(100):
    if go() > 0:
        w+=1
    else:
        l +=1

print(w, l)   