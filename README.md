# Moving-Average-Breakout
This strategy applies 5-days, 10-days and 20-days simple moving averages in order to buy stocks when it breaks above the moving averages with a bullish candlestick pattern in daily resolution. 


# Objective
The objective of this project is to test if this moving average breakout strategy can be proved to be effective and consistent. 


# Signal Generation
A buy signal is generated when the price breaks above the 5-days, 10-days and 20-days simple moving averages with a bullish candlestick patterns. Noted that the 5-days SMA should be above 10-days SMA which is also above the 20-days SMA. 


# Result
The performance is captured by only calculating its successful rate. The strategy is regarded as successful if its price does not fall under its buying price within 5 days.

First of all, the program takes the top 50 stocks in terms of trading volume throughout the backtest period. Result is shown below:

![alt text](https://github.com/kelvonlys/Moving-Average-Breakout/blob/main/S%26P%20Top%2050%20Volume.png)



Another universe is selected picking the top 50 stocks in terms of market capitalization.

![alt text](https://github.com/kelvonlys/Moving-Average-Breakout/blob/main/S%26P%20Top%2050%20Marketcap.png)




# Conclusion:
The success rate of this MA breakout strategy fluctuates over time, and it sometimes drop to as low as 30%. It seems that the method of buying the MA breakout cannot be proved to be a consistent strategy but in the meanwhile could be a profitable strategy if suitable portfolio and risk management models are applied.
