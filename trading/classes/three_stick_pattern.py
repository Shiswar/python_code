

class ThreeStickPattern(list):
    def __init_i(self, candlesticks):
        self.candlesticks = candlesticks
        self.x2 = candlesticks[2]
        self.x1 = candlesticks[1]
        self.x0 = candlesticks[0]
    
    def deliberation(self):
        # If all bullish candles
        if self.x0.bull and self.x1.bull and self.x2.bull:

            # If first 2 candles have a large body/wick ratio
            if self.x2.body_ratio >= (5/3) and self.x1.body_ratio >= (5/3):

                # If latest candle had a small body/wick ratio
                if 0.65 <= self.x0.body_ratio <= 0.85:

                    # If there was overlap in first 2 candles
                    if ( self.x2.close - self.x1.open ) / self.x2.body < 0.15:

                        return True
    
    def minima(self):
        if (self.x0.close < self.x1.close and self.x2.close < self.x1.close):
            return True
            
    def maxima (self):
        if (self.x0.close > self.x1.close and self.x2.close > self.x1.close):
            return True



