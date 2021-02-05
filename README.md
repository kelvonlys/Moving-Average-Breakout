# Moving-Average-Breakout
This strategy applies 5-days, 10-days and 20-days simple moving averages in order to buy stocks when it breaks above the moving averages with a bullish candlestick pattern in a daily resolution. 


# Objective
The objective of this project is to test if the moving average breakout strategy can be proved to be effective. 


# Signal Generation
A buy signal is generated when the price breaks above the 5-days, 10-days and 20-days simple moving averages with a bullish candlestick patterns. Noted that the 5-days SMA should be above 10-days SMA which is also above the 20-days SMA. 


# Result

The performance is captured by only calculating its successful rate. The strategy is regarded as successful if its price does not fall under its buying price within 5 days.

Since the signal seldom occurs in a daily basis, the strategy takes stocks from the pool of top 100 transaction volume in the US equity market.

Result is shown as below:


With the overall success rate over 50% with random stocks during backtest


# Conclusion:
