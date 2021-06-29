import random
import math
blacks = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
all_numbers = [0, 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31,
33, 35,1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

def is_black(number): 
    if number in blacks:
        return True
def is_red(number): 
    if number in reds:
        return True

class Selector:
    
    def __init__(self,number_of_choices, dollars_per_bet):     
        self.number_of_choices = number_of_choices
        self.dollars_per_bet = dollars_per_bet

    def random_selection(self, last):
        selections=[]
        while len(selections) < self.number_of_choices:
            random_number_idx = random.randint(0,36)
            if all_numbers[random_number_idx] not in selections and all_numbers[random_number_idx] != last:
                selections.append(random_number_idx)
        return selections

    def random_black_selections(self, last):
        selections = []
        while len(selections) < self.number_of_choices:
            random_number_idx = random.randint(0,17)
            if blacks[random_number_idx] not in selections and blacks[random_number_idx] != last :
                selections.append(blacks[random_number_idx])
        return selections
    
    def random_red_selections(self, last):
        selections = []
        while len(selections) < self.number_of_choices:
            random_number_idx = random.randint(0,17)
            if reds[random_number_idx] not in selections and reds[random_number_idx] != last:
                selections.append(reds[random_number_idx])
        return selections
    
    def same_colour_as_last(self, last):
        if is_black(last):
            return 0
        else:
            return 1
    
    
    def set_total_money(self, new_value):
        self.total_money = new_value

    def set_dollars_per_bet(self, new_value):
        self.dollars_per_bet = new_value

    def set_number_of_choices(self, new_value):
        self.number_of_choices = new_value
    



class RouletteTable:

    def __init__(self):
        self.history = [0]
        self.number = 0
        self.spin()
        
    def spin(self):
        random_number = random.randint(0,36)
        self.number = random_number
        self.history.append(random_number)

    def check_winnings(self, selections, dollars):
        if self.number in selections:
            return 36*dollars
        else: 
            return 0

    def red_or_black_winnings(self, colour, money):
        if is_black(self.number) and colour == 0:
            return money*2
        elif not is_red(self.number) and colour == 1:
            return money*2
        else:
            return 0
    





class StrategyTester:

    def __init__(self, total_money, strategy):
        self.total_money = total_money
        self.strategy = strategy
        self.table = RouletteTable()
        
    
         

    def test(self, losses_threshold, upper_threshold):
        loss_counter = 0
        win_counter = 0
        total_winnings = 0
        total_games = 0
        last = self.table.history[-1] if len(self.table.history) > 0 else random.randint(1,2)
        results = {"losses" : loss_counter,
                    "wins" : win_counter,
                    "winnings": total_winnings,
                    "games": total_games
                    }
         
        while loss_counter < losses_threshold and self.total_money < upper_threshold:
            if is_black(last):
                round_winnings = self.table.play(self.strategy.random_black_selections(), self.strategy.dollars_per_bet)
                self.total_money = self.total_money + round_winnings - self.strategy.dollars_per_bet * self.strategy.number_of_choices
                
                
            else:
                round_winnings = self.table.play(self.strategy.random_red_selections(), self.strategy.dollars_per_bet)
                self.total_money = self.total_money + round_winnings - self.strategy.dollars_per_bet * self.strategy.number_of_choices

            if round_winnings > 0:
                win_counter += 1
            else:
                loss_counter += 1
            total_games +=1
        
        results = {"losses" : loss_counter,
                    "wins" : win_counter,
                    "winnings": self.total_money,
                    "games": total_games
                    }

        return results


