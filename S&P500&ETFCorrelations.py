import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('/Users/macbookpro/Desktop/LinkedIn Work/LinkedIn Posts/S&P 500/SP500&ETF.csv', index_col='Date', parse_dates=True)

# Extract the required columns
cols = ['SP500 Returns', 'XLK_Close_Returns', 'XLV_Close_Returns', 'XLF_Close_Returns', 'XLE_Close_Returns', 'XLY_Close_Returns', 'XLRE_Close_Returns', 'XLU_Close_Returns']
df = df[cols]

# Calculate correlation coefficients
correlations = df.corr()
print(correlations)

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlations, cmap="flare", annot=True)
plt.title('Correlation Between S&P 500 and Sector ETFs')
plt.show()

'''The correlation coefficients table shows the relationship between the S&P 500 and each sector ETF.

A correlation coefficient ranges from -1 to 1, where -1 represents a perfect negative correlation, 0 represents no correlation, and 1 represents a perfect positive correlation.

In this case, we see that there is a strong positive correlation between the S&P 500 and each of the sector ETFs, with correlation coefficients ranging from 0.49 to 0.95.

The strongest correlation is between the S&P 500 and the XLK ETF (Technology), with a coefficient of 0.95. This indicates a very strong positive relationship between the two.

The XLRE ETF (Real Estate) also shows a relatively strong correlation with the S&P 500, with a coefficient of 0.81.

Overall, the correlation coefficients suggest that the performance of each sector ETF is closely tied to the performance of the S&P 500.'''