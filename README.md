# Moving-Average-Breakout
This strategy applies 5-days, 10-days and 20-days simple moving averages in order to buy stocks when it breaks above the moving averages with a bullish candlestick pattern in daily resolution. 


# Objective
The objective of this project is to test if this moving average breakout strategy can be proved to be effective and consistent. 


# Signal Generation
A buy signal is generated when the price breaks above the 5-days, 10-days and 20-days simple moving averages with a bullish candlestick patterns. Noted that the 5-days SMA should be above 10-days SMA which is also above the 20-days SMA. 


# Result
The performance is captured by only calculating its successful rate. The strategy is regarded as successful if its price does not fall under its buying price within 5 days.

Result is shown as below:

![ALT test] https://github.com/kelvonlys/Moving-Average-Breakout/blob/main/alpha.png

It can be seen that the success rate fluctuate above and below the 50% mark 


# Conclusion:
The success rate of this MA breakout strategy fluctuates over time, it seems that the method of buying the MA breakout cannot be proved to be a reliable and consistent strategy in a long-term.
