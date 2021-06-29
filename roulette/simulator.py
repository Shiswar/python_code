from classes import *
import pandas as pd


def go():
    wl = {
        "strat1":None,
        "strat2":None,
        "strat3":None
    }
    data = {
        "Number": [],
        "Money1": [],
        "Money2": [],
        "Black/Red":[]
    }

    table = RouletteTable()

    money1 = 100
    money2 = 100
    money3 = 1000

    multiplier1 = 1.65
    multiplier2 = 1.65

    bets_per_round = 10
    dollars_per_bet = 1

    s1_finished = False
    s2_finished = False
    # s3_finished = False

    upper_threshold = 200
    lower_threshold = 0

    while not(s1_finished and s2_finished):
        last = table.history[-1]
        table.spin()
        
        # Strategy 1
        # Choose random numbers each time
        if money1 > lower_threshold and money1 <= upper_threshold:
            s1 = Selector(bets_per_round,dollars_per_bet)
            selections1 = s1.random_selection(last)
            win1 = table.check_winnings(selections1, dollars_per_bet)
            money1 = money1 - (bets_per_round*dollars_per_bet) + win1
            
            
        else:
            s1_finished = True

        # Strategy 2
        # Choose random numbers of the same colour as the last roll each time
        if money2 > lower_threshold and money2 <= upper_threshold:
            s2 = Selector(bets_per_round,dollars_per_bet)
            if last == 0:
                selections2 = s2.random_selection(last)

            elif is_black(last):
                selections2 = s2.random_black_selections(last)

            else:
                selections2 = s2.random_red_selections(last)

            win2 = table.check_winnings(selections2, dollars_per_bet)
            money2 = money2 - (bets_per_round*dollars_per_bet) + win2
            
        else:
            s2_finished = True

        # Strategy 3
        # Put money on the same colour as last spin for double return
        # if money3 > lower_threshold and money3 <= upper_threshold:
        #     s3 = Selector(bets_per_round,dollars_per_bet)
        #     colour = s3.same_colour_as_last(last)
        #     win3 = table.red_or_black_winnings(colour, bets_per_round * dollars_per_bet)
        #     money3 = money3 - (bets_per_round*dollars_per_bet) + win3
        # else:
        #     s3_finished = True
        
        data["Number"].append(table.number)
        data["Money1"].append(money1)
        data["Money2"].append(money2)
        colour = "Black" if is_black(table.number) else "Red"
        data["Black/Red"].append(colour)
    
    wl["strat1"] = True if money1 > lower_threshold else False
    wl["strat2"] = True if money2 > lower_threshold else False
    # wl["strat3"] = True if money3 > lower_threshold else False
    df = pd.DataFrame(data)
    print(df)
    return wl
    
go()

    

#    while money3 > 0 and money3 <= upper_threshold and not s3_finished:
#       # Strategy 3
#        s3 = Selector(bets_per_round,dollars_per_bet)
#        win3 = table.check_winnings(selections1, dollars_per_bet)
#        money3 = money3 - (bets_per_round*dollars_per_bet) + win3