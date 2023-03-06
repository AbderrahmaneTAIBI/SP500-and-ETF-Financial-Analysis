# Report: S&P500 and ETF Financial Analysis

## Introduction:

Financial analysis is an essential aspect of investment management, where investors use different tools and techniques to assess the performance of different securities, including stocks and ETFs. The S&P 500 index is one of the widely used benchmarks for measuring the performance of the US stock market, representing the performance of 500 large-cap stocks listed on major stock exchanges in the United States. In this context, this repository contains three Python scripts that analyze the performance of the S&P 500 index and various sector ETFs.

## Dataset
All the data is scrapped from Yahoo Finance : https://finance.yahoo.com/

* The S&P 500 index is a market-cap-weighted index that includes 500 large-cap U.S. companies.

The ETF tickers are:

* XLK (Technology Select Sector SPDR Fund)
* XLV (Health Care Select Sector SPDR Fund)
* XLF (Financial Select Sector SPDR Fund)
* XLE (Energy Select Sector SPDR Fund)
* XLY (Consumer Discretionary Select Sector SPDR Fund)
* XLRE (Real Estate Select Sector SPDR Fund)
* XLU (Utilities Select Sector SPDR Fund)


## S&P500&ETF.py:

The S&P500&ETF.py script loads historical data for the S&P 500 index and several sector ETFs, merges the data, and calculates the cumulative returns for each security. The script also plots the cumulative returns for each security over time. This script helps investors to track the historical performance of different securities and compare their returns over time.

## S&P500&ETFRollingReturnsAndMovingAverages.py:

The S&P500&ETFRollingReturnsAndMovingAverages.py script loads the data generated by S&P500&ETF.py and calculates the rolling returns and moving averages for each security. It then prompts the user to select which columns to plot and plots the selected data along with the rolling returns and moving averages. The rolling returns and moving averages are commonly used to assess the trends and volatility of different securities, providing valuable insights into their future performance.

## S&P500&ETFCorrelations.py:

The S&P500&ETFCorrelations.py script loads the data generated by S&P500&ETF.py and calculates the correlations between the daily returns of each security. It then plots a heatmap of the correlation matrix. The correlation matrix helps investors to understand the interdependence between different securities, identifying which securities tend to move together and which tend to move in opposite directions.

## Conclusion:

In conclusion, financial analysis is an essential aspect of investment management, and Python is an excellent tool for analyzing financial data. The S&P500&ETF.py, S&P500&ETFRollingReturnsAndMovingAverages.py, and S&P500&ETFCorrelations.py scripts provide investors with valuable insights into the performance of the S&P 500 index and various sector ETFs, enabling them to make informed investment decisions.

### Suggestions: 
* S&P500 & ETF Diversification
* S&P500 & ETF Performance Comparison
* S&P500 & ETF Market Sentiment
