import pandas as pd
import matplotlib.pyplot as plt

# Load S&P 500 data
sp500_df = pd.read_csv('/Users/macbookpro/Desktop/LinkedIn Work/LinkedIn Posts/S&P 500/S&P500history.csv', sep=';')
sp500_df['Date'] = pd.to_datetime(sp500_df['Date'], format='%b %d, %Y')
sp500_df['Close*'] = sp500_df['Close*'].str.replace(',', '').astype(float)

# Load sector ETF data
sector_etfs = ['XLK', 'XLV', 'XLF', 'XLE', 'XLY', 'XLRE', 'XLU']
dfs = []
for sector in sector_etfs:
    sector_df = pd.read_csv(f'/Users/macbookpro/Desktop/LinkedIn Work/LinkedIn Posts/S&P 500/{sector}.csv')
    sector_df['Date'] = pd.to_datetime(sector_df['Date'], format='%Y-%m-%d')
    sector_df.set_index('Date', inplace=True)
    dfs.append(sector_df.add_prefix(f'{sector}_'))
sector_df = pd.concat(dfs, axis=1)

# Merge sector-specific ETF data with S&P 500 data
merged_df = pd.merge(sp500_df, sector_df, on='Date', how='inner')

merged_df.to_csv('/Users/macbookpro/Desktop/LinkedIn Work/LinkedIn Posts/S&P 500/SP500&ETF.csv')

# Calculate returns and cumulative returns
merged_df['SP500 Returns'] = merged_df['Close*'].pct_change()
merged_df['SP500 Cumulative Returns'] = (1 + merged_df['SP500 Returns']).cumprod() - 1

print(merged_df.shape)


# Calculate returns and cumulative returns for each sector
sector_close_cols = ['XLK_Close', 'XLV_Close', 'XLF_Close', 'XLE_Close', 'XLY_Close', 'XLRE_Close', 'XLU_Close']
sector_returns = merged_df[sector_close_cols].pct_change()
sector_cumulative_returns = (1 + sector_returns).cumprod() - 1

# Append results to merged_df
merged_df = pd.concat([merged_df, sector_returns.add_suffix('_Returns'), sector_cumulative_returns.add_suffix('_Cumulative_Returns')], axis=1)

merged_df.to_csv('/Users/macbookpro/Desktop/LinkedIn Work/LinkedIn Posts/S&P 500/SP500&ETF.csv')

# Plot cumulative returns
plt.plot(merged_df['Date'], merged_df['SP500 Cumulative Returns'])
plt.plot(merged_df['Date'], merged_df['XLK_Close_Cumulative_Returns'])
plt.plot(merged_df['Date'], merged_df['XLV_Close_Cumulative_Returns'])
plt.plot(merged_df['Date'], merged_df['XLF_Close_Cumulative_Returns'])
plt.plot(merged_df['Date'], merged_df['XLE_Close_Cumulative_Returns'])
plt.plot(merged_df['Date'], merged_df['XLY_Close_Cumulative_Returns'])
plt.plot(merged_df['Date'], merged_df['XLRE_Close_Cumulative_Returns'])
plt.plot(merged_df['Date'], merged_df['XLU_Close_Cumulative_Returns'])
plt.title('Cumulative Returns of S&P 500 and Sectors')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.legend(['SP500', 'XLK', 'XLV', 'XLF', 'XLE', 'XLY', 'XLRE', 'XLU'])
plt.show(block=True)

