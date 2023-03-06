import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('/Users/macbookpro/Desktop/LinkedIn Work/LinkedIn Posts/S&P 500/SP500&ETF.csv', index_col='Date', parse_dates=True)

# Extract the required columns
cols = ['SP500 Cumulative Returns', 'XLK_Close_Cumulative_Returns', 'XLV_Close_Cumulative_Returns', 'XLF_Close_Cumulative_Returns', 'XLE_Close_Cumulative_Returns', 'XLY_Close_Cumulative_Returns', 'XLRE_Close_Cumulative_Returns', 'XLU_Close_Cumulative_Returns']
df = df[cols]

# Calculate rolling returns and moving averages
rolling_returns = df.rolling(window=20).mean()
moving_averages = df.rolling(window=50).mean()

# Allow user to choose which columns to plot
print('Which columns do you want to plot?')
print(cols)
user_cols = input('Enter column(s) separated by commas or enter "all" to plot all columns: ').split(',')
if 'all' in user_cols:
    user_cols = cols
df = df[user_cols]
rolling_returns = rolling_returns[user_cols]
moving_averages = moving_averages[user_cols]

# Plot the data
plt.figure(figsize=(12, 8))
plt.plot(df)
plt.plot(rolling_returns)
plt.plot(moving_averages)
plt.legend(user_cols + ['Rolling Returns', 'Moving Averages'])
plt.title('Cumulative Returns with Rolling Returns and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.show()
