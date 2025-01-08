import pandas as pd
file_path = 'finish.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data to understand its structure
data.head()

# Create a pivot table to analyze the relationship between crime types
# Group by 'type' and 'oc_region' to identify overlaps
crime_region_pivot = data.pivot_table(index='oc_region', columns='type', aggfunc='size', fill_value=0)

# Calculate correlation between crime types
crime_type_correlation = crime_region_pivot.corr()

# Display the correlation matrix and visualize it as a heatmap
import matplotlib.pyplot as plt

# Step 1: Calculate annual trends for overall and type-specific crime counts
annual_trends = data.groupby(['oc_year'])['oc_data'].count()
type_trends = data.groupby(['oc_year', 'type'])['oc_data'].count().unstack()

# Plot overall crime trend
plt.figure(figsize=(15, 10))
annual_trends.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Overall Crime Count by Year", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Crime Count", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

import seaborn as sns
from matplotlib import rcParams
# 設定字體讓plt文字能正常顯示
rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題
# 假设 crime_type_correlation 是你的数据框
plt.figure(figsize=(12, 8))
sns.heatmap(crime_type_correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Crime Types", fontsize=14)

# 使用自定義標籤函數
plt.xticks(ticks=range(len(crime_type_correlation.columns)), 
             labels=[col[:7] for col in crime_type_correlation.columns],
             rotation=0, ha='right', fontsize=12)

plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()