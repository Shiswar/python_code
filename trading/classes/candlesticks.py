

from numpy.core.numeric import ones


class CandleGroup:
    
    def __init__(self, open:list, high:list, low:list, close:list, volume:list ):
        self.candles = []
        
        for i in range(len(close)):
            self.candles.append(
                self.Candle(
                    open[i], 
                    high[i], 
                    low[i], 
                    close[i],
                    volume[i]
                )
            )
        self.size = len(self.candles)

    
    def get_maxima_indexes_5(self):
        indexes = []
        for i in range(2, self.size - 2):
            if (( self.candles[i-2].close < self.candles[i-1].close ) and 
                ( self.candles[i-1].close < self.candles[i].close ) and 
                (self.candles[i].close > self.candles[i+1].close) and 
                (self.candles[i+1].close > self.candles[i+2].close)):

                indexes.append(i)
        return indexes
    
    def get_minima_indexes_5(self):
        indexes = []
        for i in range(2, self.size - 2):
            if (( self.candles[i-2].close > self.candles[i-1].close ) and 
                ( self.candles[i-1].close > self.candles[i].close ) and 
                (self.candles[i].close < self.candles[i+1].close) and 
                (self.candles[i+1].close < self.candles[i+2].close)):

                indexes.append(i)
        return indexes
    
    def get_three_green_candles(self):
        indexes = []
        for i in range(self.size - 2):
            if self.candles[i].bull() and  self.candles[i+1].bull() and self.candles[i+2].bull():
                indexes.append(i)
        return indexes
    
    def get_bearish_engulfing_2(self):
        indexes = []
        for i in range(self.size - 1):
            one = self.candles[i+1]
            two = self.candles[i]
            if one.bull() and two.bear():
                if one.close <= two.open and one.open > two.close:
                    indexes.append(i)
                    print(one.close, two.open, one.open, two.close)
        return indexes
    
    def hanging_man_5(self):
        indexes = []
        for i in range(2, self.size - 2):
            one = self.candles[i+2]
            two = self.candles[i+1]
            three = self.candles[i]
            four = self.candles[i-1]
            five = self.candles[i-2]
            if one.bull() and two.bull() and three.bull() and four.bear() and five.bear():
                # if four.bot_wick_ratio() >= 5 and four.top_wick_ratio() < 1:
                indexes.append(i)
        return indexes


    class Candle:
        def __init__(self, open, high, low, close, volume):
            self.open = open
            self.high = high
            self.low = low
            self.close = close
            self.volume = volume

        def body(self):
            return abs(self.open-self.close)
        
        def topwick_size(self):
            return self.high - max(self.open, self.close)
        
        def botwick_size(self):
            return max(self.open, self.close) - self.low

        def wick_size(self):
            return (self.topwick_size + self.botwick_size)    

        def wick_ratio(self):
            return (self.wick_size) / self.body
        
        def body_ratio(self):
            return self.body / (self.wick_size)
        
        def top_wick_ratio(self):
            return self.topwick_size() / self.body()
        
        def bot_wick_ratio(self):
            return self.botwick_size() / self.body()

        def grade():
            #TODO Work on a grading function. Iclude volume and candle shape measurements
            return
        
        def bull(self):
            return self.close > self.open
        
        def bear(self):
            return self.close < self.open


class ThreeStickPattern(CandleGroup):
    def __init__(self, open:list, high:list, low:list, close:list):
        super().__init__(open, high, low, close)
    
    def deliberation(self):
        # If all bullish candles
        if self.candles[0].bull() and self.candles[1].bull() and self.candles[2].bull():

            # If first 2 candles have a large body/wick ratio
            # if self.x2.body_ratio >= (5/3) and self.x1.body_ratio >= (5/3):

            #     # If latest candle had a small body/wick ratio
            #     if 0.65 <= self.x0.body_ratio <= 0.85:

            #         # If there was overlap in first 2 candles
            #         if ( self.x2.close - self.x1.open ) / self.x2.body < 0.15:

            #             return True
            print("yes")
    
    # def minima(self):
    #     if (self.x0.close < self.x1.close and self.x2.close < self.x1.close):
    #         return True
            
    # def maxima (self):
    #     if (self.x0.close > self.x1.close and self.x2.close > self.x1.close):
    #         return True





