import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'finish.csv'
data = pd.read_csv(file_path)

# 按 "type"和 "oc_region"分組，查看重疊情況
crime_region_pivot = data.pivot_table(index='oc_region', columns='type', aggfunc='size', fill_value=0)

# 計算之間的相關性
crime_type_correlation = crime_region_pivot.corr()
print(crime_type_correlation)

# 熱力圖
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
plt.figure(figsize=(15, 8))
sns.heatmap(crime_type_correlation, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
plt.title("Correlation", size=32)
plt.show()