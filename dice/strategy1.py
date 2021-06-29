import math
import random
import time

def go(m, l, u, b):
    money = m
    lower_bound = l
    upper_bound = u

    loss_count = 0
    win_count = 0

    loss_run = 0

    lowest, highest = money, money
    
    won_last = True

    ov_un = 1

    reset = b
    bet_amount = reset

    bet_multiplier = 1.25

    number_of_bets = 0

    print()

    def play(bet, ov_un):
        spin = random.randint(0, 100)
        if ov_un == 1:
            if spin >= 80:
                return bet * 4.95
        else:
            if spin <= 20:
                return bet * 4.95
        return 0

    while money >= lower_bound and money <= upper_bound:
        
        # Over under switch
        if loss_count == 5:
            ov_un = 1-ov_un
            loss_count = 0
        if win_count == 10:
            ov_un = 1-ov_un
            win_count = 0
        
        # Play bet and get result
        result = play(bet_amount, ov_un)
        money = money - bet_amount + result
        
        # Win or loss check, reset or increase bet
        if result > 0:
            bet_amount = reset
            win_count += 1
            loss_run = 0
        else:
            bet_amount = bet_amount * bet_multiplier
            loss_count += 1
            loss_run += 1

        # Track lows and highs
        if money < lowest:
            lowest = money
        elif money > highest:
            highest = money
        
        #Count amount of bets
        number_of_bets += 1

        # time.sleep(0.01)
    return (money, highest, lowest, number_of_bets)

w = 0
l = 0

av_hi = 0
av_lo = 0

hist = []

num = 0
profit = 0

starting_cash = 50
loss_cutoff = 40
win_cutoff = 55
bet = 0.005

for i in range(5):
    m, hi, lo, n = go(starting_cash, loss_cutoff, win_cutoff, bet)
    if m <= loss_cutoff:
        l += 1
        av_hi += hi
        hist.append("L")
        profit -= (starting_cash - loss_cutoff)
    else:
        w += 1
        av_lo += lo
        hist.append("W")
        profit += (win_cutoff - starting_cash)
    num += n
    


# Safest:
# starting_cash = 50
# loss_cutoff = 55
# win_cutoff = 40
# bet = 0.005


print("Wins:",w,"Losses", l)
print("%Wins",w/(w+l))
print("Average high on loss", av_hi/l if l > 0 else av_hi)
print("Average low on win", av_lo/w if w > 0 else av_lo)
print("Average number of bets", num/(w+l))
print(hist)
print(profit) 