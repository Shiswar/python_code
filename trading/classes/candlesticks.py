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
        return self.topwick_size / self.body
    
    def bot_wick_ratio(self):
        return self.botwick_size / self.body

    def grade():
        #TODO Work on a grading function. Iclude volume and candle shape measurements
        return
    
    def bull(self):
        return self.close > self.open
    
    def bear(self):
        return self.close < self.open
