import random


def play(bet, over):
        spin = random.randint(0, 100)
        if over:
            if spin >= 80:
                return bet * 4.95
        else:
            if spin <= 20:
                return bet * 4.95
        return 0

net_profit = 0

for i in range(20):
    bank = 0

    balance = 140
    # base_bet = 0.000206
    # base_bet = 0.0005
    # base_bet = 0.0006
    base_bet = 0.0008

    print("Base bet:", base_bet)
    bet_multiplier = 1.25
    current_bet = base_bet

    total_bets = 0
    freq_list = [[x,0] for x in range(60)]

    loss_streak = 0
    win_streak = 0

    over = True

    
    while balance > current_bet and total_bets <= 1000000:
        result = play(current_bet, over)
        total_bets += 1 

        if result == 0:
            #Loss
            balance = balance - current_bet
            current_bet = current_bet * bet_multiplier

            win_streak = 0
            loss_streak += 1

            
        else:
            #Win
            balance = balance + result
            current_bet = base_bet
            win_streak += 1
            loss_streak = 0
            
            freq_list[loss_streak][1] += 1
        
        if balance >= 150:
            bank += 10
            balance -= 10

        elif balance < current_bet:
            if bank >= 140:
                loss_streak = 0
                current_bet = base_bet
                balance += 140
                bank -= 140
    net_profit += bank-140
    
            

    print("balance:",balance)
    print("bank:",bank)
    print("after rebuy:", bank-140)
    print("total_bets:",total_bets)
    # print("per hour:", bank/(total_bets/2800))
    print(net_profit)
