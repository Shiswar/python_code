import math

import random
import time

money = 50
bet = 0.05
original_bet = 0.05

max = 0

total_wins = 0
total_losses = 0
loss_count = 0
chosen_colour = 1

multiplier = 1.65

lower_bound = 0
upper_bound = 300

won_last = True

loss_list = [0 for x in range(17)]

def play(bet, colour):
    spin = random.randint(0, 100)
    if spin >= 55:
        return bet * 2.2
    else:
        return 0


while money > lower_bound and loss_count <= 16:

    if won_last:
        bet = original_bet
        winnings = play(bet, chosen_colour)
        if winnings > 0:
            won_last = True
            loss_list[loss_count] += 1
            loss_count=0
            total_wins += 1
        else:
            loss_count += 1
            total_losses += 1
            won_last = False
        money = money - bet + winnings

    else:

        bet = bet * multiplier
        winnings = play(bet, chosen_colour)
        if winnings > 0:
            won_last = True
            loss_list[loss_count] += 1
            loss_count=0
            total_wins += 1
            
        else:
            loss_count += 1
            total_losses += 1
            won_last = False
        money = money - bet + winnings


    if money > max:
        max = money


    # if chosen_colour == 1:
    #     chosen_colour = 0
    # else:
    #     chosen_colour = 1
    # print("Win?: ",won_last, end="    ")
    # print("Cash: ",money, end="    ")
    # print("Bet: ",bet)

print("Cash:",money)
print("Max:",max)
print("Total wins:", total_wins)
print("Total losses:", total_losses)
print("WIn%:",total_wins/(total_losses + total_wins))
print(loss_list)





