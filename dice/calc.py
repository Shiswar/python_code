import pandas as pd


data = {
    "# Losses":[],
    "Total lost":[],
    "Next bet:":[],
    "Profit on win":[]
}

bet= 0.00062
total_losses=0
chance = 0.20
multiplier = 1.25
payout_multiplier = 4.95

for i in range(60):
    data["# Losses"].append(i)
    data["Total lost"].append(total_losses)
    data["Next bet:"].append(bet*(multiplier**i))
    # data["Profit on win"].append(chance**i)
    if i>0:
        data["Profit on win"].append((bet*(multiplier**i)*payout_multiplier)-total_losses)
    else:
        data["Profit on win"].append(0)
    

    #print3("# Losses:",i,"Total lost: ",total_losses,"Next bet: ", bet*(1.65**i), "Chance:",chance**i)
    total_losses += bet*(multiplier**i)


df = pd.DataFrame(data)
print(df)

# 50 49 50 52 48 45