# This is entirely the work of Shae Iswar as a submission for TCS CodeVita
# A piece of code that resembles a dice rolling game.
# An S sided dice is rolled, whatever the result of the roll is (lets call it r), an r sided dice will be rolled.
# This process continues untill a 1 is rolled, and the number of rolls it tool to roll a 1 is recorded.
# This game is played 10000 times and the average number of rolles is taken
# The output is the minimum of 10 x 10000 game simulations.

import math, random, statistics



def my_mean(data):
    sm = 0
    for n in data:
        sm += n
    return sm/(len(data))

s = int(input(""))


count_list =[ [] for i in range(10) ]

ind = 0
for k in range(10):
    
    for j in range(10000):
        s_temp = s
        count = 0
        while s_temp != 1:
            r = random.randint(1,s_temp)
            count += 1
            s_temp = r
        count_list[ind].append(count)
    ind += 1


averages = []
for l in count_list:
    averages.append(round(my_mean(l)))
print(min(averages))






